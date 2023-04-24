"""Module """
from .order_request import OrderRequest
from .order_shipping import OrderShipping
from .order_delivered import OrderDelivered
from .json_store_order import JsonOrderStore

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

        my_order.crear_json()
        return my_order.order_id


    #pylint: disable=too-many-locals
    def send_product (self, input_file:str )->str:
        """Sends the order included in the input_file"""
        my_sign = OrderShipping(input_file)
        my_sign.crear_json()
        return my_sign.tracking_code


    def deliver_product(self, tracking_code:str)->True:
        """Register the delivery of the product"""
        my_deliver = OrderDelivered(tracking_code)
        my_deliver.crear_json()
        return True