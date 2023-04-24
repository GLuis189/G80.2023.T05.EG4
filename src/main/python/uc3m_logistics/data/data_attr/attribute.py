
import re
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class Attribute():
    def __init__(self)->None:
        self._attr_value= ""
        self._error_message = ""
        self._validation_pattern = r""


    def _validate(self, value:str)->str:
        myregex = re.compile(self._validation_pattern)
        result = myregex.fullmatch(value)
        if not result:
            raise OrderManagementException(self._error_message)
        return value

    @property
    def value(self)->str:
        return self._attr_value

    @value.setter
    def value(self, attr_value:str)->None:
        self._attr_value = attr_value

