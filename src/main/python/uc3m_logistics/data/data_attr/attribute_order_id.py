from uc3m_logistics.data.data_attr.attribute import Attribute

class OrderId(Attribute):
    def __init__(self, attr_value:str)->None:
        self._error_message = "order id is not valid"
        self._validation_pattern = r"[0-9a-fA-F]{32}$"
        self._attr_value = self._validate(attr_value)