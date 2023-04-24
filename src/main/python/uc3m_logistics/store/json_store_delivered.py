"""MODULES"""
from uc3m_logistics.store.json_store_master import JsonStoreMaster
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH

class JsonDeliverStore(JsonStoreMaster):
    """Clase JsonDeliverStore"""
    _FILE_PATH = JSON_FILES_PATH + "shipments_delivered.json"
    _data_list = []
    _ID_FIELD = ""

    __instance = None
    def __new__(cls):
        """Patrón Singleton"""
        if JsonDeliverStore.__instance is None:
            JsonDeliverStore.__instance = object.__new__(cls)
        return JsonDeliverStore.__instance
    def __init__(self)->None:
        """Constructor de JsonDeliverStore"""
        super(JsonStoreMaster, self).__init__()
