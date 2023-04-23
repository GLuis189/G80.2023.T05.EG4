"""Module """
import datetime
import re
import json
from datetime import datetime
from freezegun import freeze_time
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_delivered import OrderDelivered
from .order_manager_config import JSON_FILES_PATH
from .json_store import JsonStore
from .json_store_order import JsonOrderStore
from .json_store_shipments import JsonShipmentsStore
class OrderManager:
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        pass

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
        my_store =JsonOrderStore()
        my_store.add_item(my_order)

        return my_order.order_id


    #pylint: disable=too-many-locals
    def send_product (self, input_file:str )->str:
        """Sends the order included in the input_file"""

        my_sign= OrderShipping(input_file)

        my_ship_store = JsonShipmentsStore()
        my_ship_store.add_item(my_sign.__dict__)


        return my_sign.tracking_code


    def deliver_product(self, tracking_code:str)->True:
        """Register the delivery of the product"""
        my_deliver = OrderDelivered(tracking_code)

        my_ship_store = JsonStore()

        #check if this tracking_code is in shipments_store
        data_list = my_ship_store.read_shipping_store()

        del_timestamp = my_ship_store.find_tracking_code(data_list, tracking_code)

        my_ship_store.check_date(del_timestamp)
        my_ship_store.save_delivere_store(my_deliver)
        return True


