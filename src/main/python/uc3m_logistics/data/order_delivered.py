"""MODULES"""
from datetime import datetime, date
from uc3m_logistics.data.data_attr.attribute_tracking_code import Tracking_code
from uc3m_logistics.store.json_store_shipments import JsonShipmentsStore
from uc3m_logistics.store.json_store_delivered import JsonDeliverStore
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class OrderDelivered():
    """Clase OrderDelivered"""
    def __init__(self, tracking_code:str)->None:
        """Constructor OrderDelivered"""
        self.__tracking_code = Tracking_code(tracking_code).value
        self.__date_delivered = datetime.utcnow().__str__()
        del_timestamp = self.check_tracking_code(tracking_code)
        self.check_date(del_timestamp)


    def check_tracking_code(self, tracking_code:str)->float:
        """Comprueba el tracking code"""
        # check if this tracking_code is in shipments_store
        my_ship_store = JsonShipmentsStore()
        my_ship_store.read_store()
        item_found = my_ship_store.find_data(tracking_code)
        if item_found:
            del_timestamp = item_found["_OrderShipping__delivery_day"]
        else:
            raise OrderManagementException("tracking_code is not found")
        return del_timestamp

    def check_date(self, del_timestamp:float)->date:
        """Comprueba la fecha"""
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
        return today

    def crear_json(self)->None:
        """Crea el json"""
        my_deliver_store = JsonDeliverStore()
        my_deliver_store.add_item(self)
