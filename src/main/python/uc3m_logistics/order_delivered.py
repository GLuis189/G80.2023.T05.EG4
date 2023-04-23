from datetime import datetime
from .attribute_tracking_code import Tracking_code
from .json_store_shipments import JsonShipmentsStore
from .order_management_exception import OrderManagementException

class OrderDelivered():
    def __init__(self, tracking_code):
        self.__tracking_code = Tracking_code(tracking_code).value
        self.__date_delivered = datetime.utcnow().__str__()
        del_timestamp = self.check_tracking_code(tracking_code)
        self.check_date(del_timestamp)

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