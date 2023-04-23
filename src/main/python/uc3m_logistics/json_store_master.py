import json
from .order_management_exception import OrderManagementException


class JsonStoreMaster():
    _FILE_PATH = ""
    _data_list = []
    _ID_FIELD = ""

    def __init__(self):
        self.load_store()

    def load_store(self):
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
    def save_store(self):
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

    def find_data(self, data_to_find):
        item_found = None
        for item in self._data_list:
            if item[self._ID_FIELD] == data_to_find:
                item_found = item
        return item_found

    def add_item(self, item):
        self.load_store()
        self._data_list.append(item.__dict__)
        self.save_store()