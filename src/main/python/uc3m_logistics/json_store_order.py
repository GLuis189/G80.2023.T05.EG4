from .json_store_master import JsonStoreMaster
from .order_manager_config import JSON_FILES_PATH
from .order_management_exception import OrderManagementException

class JsonOrderStore(JsonStoreMaster):
    _FILE_PATH = JSON_FILES_PATH + "orders_store.json"
    _data_list = []
    _ID_FIELD = "_OrderRequest__order_id"
    def __init__(self):
        pass
    def add_item(self, item):
        self.load_store()
        item_found = self.find_data(item.order_id)
        if item_found is None:
            self._data_list.append(item.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        self.save_store()

