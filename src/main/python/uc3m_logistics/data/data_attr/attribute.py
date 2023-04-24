"""MODULES"""
import re
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class Attribute():
    """Clase padre atributo"""
    def __init__(self)->None:
        self._attr_value= ""
        self._error_message = ""
        self._validation_pattern = r""


    def _validate(self, attr_value:str)->str:
        """Función validación"""
        myregex = re.compile(self._validation_pattern)
        result = myregex.fullmatch(attr_value)
        if not result:
            raise OrderManagementException(self._error_message)
        return attr_value

    @property
    def value(self)->str:
        """Property"""
        return self._attr_value

    @value.setter
    def value(self, attr_value:str)->None:
        """Setter"""
        self._attr_value = attr_value
