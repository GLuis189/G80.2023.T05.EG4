"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class PhoneNumber(Attribute):
    """Clase hija, atributo PhoneNumber"""
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = "phone number is not valid"
        self._validation_pattern = r"^(\+)[0-9]{11}"
        self._attr_value = self._validate(attr_value)
