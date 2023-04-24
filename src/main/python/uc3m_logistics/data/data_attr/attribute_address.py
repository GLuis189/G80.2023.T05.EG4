"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class Address(Attribute):
    """Clase hija, atributo address"""
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = "address is not valid"
        self._validation_pattern = r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$"
        self._attr_value = self._validate(attr_value)
