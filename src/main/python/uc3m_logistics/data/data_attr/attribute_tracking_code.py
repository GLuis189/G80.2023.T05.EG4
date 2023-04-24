"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute

class TrackingCode(Attribute):
    """Clase hija, atributo tracking code"""
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = "tracking_code format is not valid"
        self._validation_pattern = r"[0-9a-fA-F]{64}$"
        self._attr_value = self._validate(attr_value)
