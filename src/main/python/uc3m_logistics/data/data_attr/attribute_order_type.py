"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class OrderType(Attribute):
    """Clase hija,atributo OrderType"""
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = "order_type is not valid"
        self._validation_pattern = r"(Regular|Premium)"
        self._attr_value = self._validate(attr_value)
