"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class Address(Attribute):
    """Clase hija, atributo address"""
    __ERROR = "address is not valid"
    __PATTERN = r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$"
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = self.__ERROR
        self._validation_pattern = self.__PATTERN
        self._attr_value = self._validate(attr_value)
