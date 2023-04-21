"""Module """
import datetime
import re
import json
from datetime import datetime
from freezegun import freeze_time
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_manager_config import JSON_FILES_PATH
from .json_store import JsonStore

class OrderManager:
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_tracking_code(tracking_code: str)->None:
        """Method for validating sha256 values"""
        myregex = re.compile(r"[0-9a-fA-F]{64}$")
        result = myregex.fullmatch(tracking_code)
        if not result:
            raise OrderManagementException("tracking_code format is not valid")



    #pylint: disable=too-many-arguments
    def register_order(self, product_id:str,
                        order_type:str,
                        address:str,
                        phone_number:str,
                        zip_code:str)->str:
        """Register the orders into the order's file"""


        my_order = OrderRequest(product_id,
                                order_type,
                                address,
                                phone_number,
                                zip_code)

        #self.save_store(my_order)
        my_store =JsonStore()
        my_store.save_store(my_order)

        return my_order.order_id


    #pylint: disable=too-many-locals
    def send_product (self, input_file:str )->str:
        """Sends the order included in the input_file"""

        my_sign= OrderShipping(input_file)

        my_ship_store = JsonStore
        my_ship_store.save_orders_shipped(my_sign)


        return my_sign.tracking_code


    def deliver_product(self, tracking_code:str)->True:
        """Register the delivery of the product"""
        self.validate_tracking_code(tracking_code)

        #check if this tracking_code is in shipments_store
        data_list = self.read_shipping_store()

        del_timestamp = self.find_tracking_code(data_list, tracking_code)

        self.check_date(del_timestamp)

        self.save_delivere_store(tracking_code)
        return True

    def save_delivere_store(self, tracking_code):
        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"
        try:
            with open(shipments_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

            # append the delivery info
        data_list.append(str(tracking_code))
        data_list.append(str(datetime.utcnow()))
        try:
            with open(shipments_file, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

    def check_date(self, del_timestamp):
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")

    def find_tracking_code(self, data_list, tracking_code):
        # search this tracking_code
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")
        return del_timestamp

    def read_shipping_store(self):
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex
        return data_list
