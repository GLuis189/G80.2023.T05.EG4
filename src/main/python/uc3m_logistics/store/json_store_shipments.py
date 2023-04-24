"""MODULES"""
import json
from uc3m_logistics.store.json_store_master import JsonStoreMaster
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class JsonShipmentsStore(JsonStoreMaster):
    """Clase JsonShipment"""
    _FILE_PATH = JSON_FILES_PATH + "shipments_store.json"
    _data_list = []
    _ID_FIELD = "_OrderShipping__tracking_code"
    __instance = None
    def __new__(cls):
        if JsonShipmentsStore.__instance is None:
            JsonShipmentsStore.__instance = object.__new__(cls)
        return JsonShipmentsStore.__instance
    def __init__(self)->None:
        """Constructor de JsonDeliverStore"""
        super(JsonStoreMaster, self).__init__()
    def read_store(self)->any:
        """Leer"""
        # first read the file
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex
        return self._data_list
