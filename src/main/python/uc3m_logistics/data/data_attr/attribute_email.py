"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class Email(Attribute):
    """Clase hija, atributo email"""
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = "contact email is not valid"
        self._validation_pattern = r"^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$"
        self._attr_value = self._validate(attr_value)
