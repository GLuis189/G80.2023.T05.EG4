"""Contains the class OrderShipping"""
import hashlib
import re
import json
from datetime import datetime
from freezegun import freeze_time
from .order_management_exception import OrderManagementException
from .order_manager_config import JSON_FILES_PATH
from .order_request import OrderRequest
from .attribute_email import Email
from .attribute_order_id import OrderId
from.json_store_shipments import JsonShipmentsStore

#pylint: disable=too-many-instance-attributes
class OrderShipping():
    """Class representing the shipping of an order"""

    def __init__(self, input_file):
        self.__json_content = self.read_json_file(input_file)
        self.__mydelivery_email,self.__myorder_id = self.validate_labels(self.__json_content)
        self.__order_id = OrderId(self.__myorder_id).value
        self.__delivery_email = Email(self.__mydelivery_email).value
        self.__myproduct_id, self.__myorder_type = self.check_order_id(self.__json_content)
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__product_id = self.__myproduct_id
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if self.__myorder_type == "Regular":
            delivery_days = 7
        else:
            delivery_days = 1
        #timestamp is represneted in seconds.microseconds
        #__delivery_day must be expressed in senconds to be added to the timestap
        self.__delivery_day = self.__issued_at + (delivery_days * 24 * 60 * 60)
        self.__tracking_code = hashlib.sha256(self.__signature_string().encode()).hexdigest()
        my_ship_store = JsonShipmentsStore()
        my_ship_store.add_item(self)

    def __signature_string( self ):
        """Composes the string to be used for generating the tracking_code"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",order_id:" + \
               self.__order_id + ",issuedate:" + str(self.__issued_at) + \
               ",deliveryday:" + str(self.__delivery_day) + "}"

    @property
    def product_id( self ):
        """Property that represents the product_id of the order"""
        return self.__product_id

    @product_id.setter
    def product_id( self, value ):
        self.__product_id = value

    @property
    def order_id( self ):
        """Property that represents the order_id"""
        return self.__order_id

    @order_id.setter
    def order_id( self, value ):
        self.__order_id = value

    @property
    def email( self ):
        """Property that represents the email of the client"""
        return self.__delivery_email

    @email.setter
    def email( self, value ):
        self.__delivery_email = value

    @property
    def tracking_code( self ):
        """returns the tracking code"""
        return self.__tracking_code

    @property
    def issued_at( self ):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at( self, value ):
        self.__issued_at = value

    @property
    def delivery_day( self ):
        """Returns the delivery day for the order"""
        return self.__delivery_day

    def read_json_file(self, input_file):
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as exception:
            # file is not found
            raise OrderManagementException("File is not found") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
        return data

    def validate_labels(self, data):
        try:
            order_id = data["OrderID"]
            email = data["ContactEmail"]
        except KeyError as exception:
            raise OrderManagementException("Bad label") from exception
        return email, order_id

    def check_order_id(self, data):
        file_store = JSON_FILES_PATH + "orders_store.json"
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data["OrderID"]:
                found = True
                # retrieve the orders data
                product_id = item["_OrderRequest__product_id"]
                address = item["_OrderRequest__delivery_address"]
                register_type = item["_OrderRequest__order_type"]
                phone = item["_OrderRequest__phone_number"]
                order_timestamp = item["_OrderRequest__time_stamp"]
                zip_code = item["_OrderRequest__zip_code"]
                # set the time when the order was registered for checking the md5
                with freeze_time(datetime.fromtimestamp(order_timestamp).date()):
                    order = OrderRequest(product_id=product_id,
                                         delivery_address=address,
                                         order_type=register_type,
                                         phone_number=phone,
                                         zip_code=zip_code)

                if order.order_id != data["OrderID"]:
                    raise OrderManagementException("Orders' data have been manipulated")
        if not found:
            raise OrderManagementException("order_id not found")
        return product_id, register_type