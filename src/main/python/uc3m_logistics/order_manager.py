"""Module """
import datetime
from datetime import datetime
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_delivered import OrderDelivered
from .json_store_order import JsonOrderStore
from .json_store_shipments import JsonShipmentsStore
from .json_store_delivered import JsonDeliverStore
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

        my_store =JsonOrderStore()
        my_store.add_item(my_order)

        return my_order.order_id


    #pylint: disable=too-many-locals
    def send_product (self, input_file:str )->str:
        """Sends the order included in the input_file"""

        my_sign= OrderShipping(input_file)

        my_ship_store = JsonShipmentsStore()
        my_ship_store.add_item(my_sign)


        return my_sign.tracking_code


    def deliver_product(self, tracking_code:str)->True:
        """Register the delivery of the product"""
        my_deliver = OrderDelivered(tracking_code)

        del_timestamp = self.check_tracking_code(tracking_code)

        self.check_date(del_timestamp)

        my_deliver_store = JsonDeliverStore()
        my_deliver_store.add_item(my_deliver)

        return True

    def check_tracking_code(self, tracking_code):
        # check if this tracking_code is in shipments_store
        my_ship_store = JsonShipmentsStore()
        data_list = my_ship_store.read_store()
        item_found = my_ship_store.find_data(tracking_code)
        if item_found:
            del_timestamp = item_found["_OrderShipping__delivery_day"]
        else:
            raise OrderManagementException("tracking_code is not found")
        return del_timestamp

    def check_date(self, del_timestamp):
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
        return today

