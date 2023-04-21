"""Contains the class OrderShipping"""
import hashlib
import re
import json
from datetime import datetime
from .order_management_exception import OrderManagementException

#pylint: disable=too-many-instance-attributes
class OrderShipping():
    """Class representing the shipping of an order"""

    def __init__(self, input_file):
        self.__json_content = self.read_json_file(input_file)
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__product_id = product_id
        self.__order_id = self.validate_order_id(order_id)
        self.__delivery_email = self.validate_email(delivery_email)
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if order_type == "Regular":
            delivery_days = 7
        else:
            delivery_days = 1
        #timestamp is represneted in seconds.microseconds
        #__delivery_day must be expressed in senconds to be added to the timestap
        self.__delivery_day = self.__issued_at + (delivery_days * 24 * 60 * 60)
        self.__tracking_code = hashlib.sha256(self.__signature_string().encode()).hexdigest()

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

    def validate_order_id(self, order_id:str)->str:
        myregex = re.compile(r"[0-9a-fA-F]{32}$")
        result = myregex.fullmatch(order_id)
        if not result:
            raise OrderManagementException("order id is not valid")
        return order_id

    def validate_email(self, email:str)->str:
        regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'
        myregex = re.compile(regex_email)
        result = myregex.fullmatch(email)
        if not result:
            raise OrderManagementException("contact email is not valid")

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