from uc3m_logistics.data.data_attr.attribute import Attribute
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class ZipCode(Attribute):
    def __init__(self, attr_value:str)->None:
        self._error_message = "zip_code format is not valid"
        self._validation_pattern = r"[0-9]{5}"
        self._attr_value = self.validate_zip_code(attr_value)

    def validate_zip_code(self, attr_value:str)->str:
        super()._validate(attr_value)
        if (int(attr_value) > 52999 or int(attr_value) < 1000):
            raise OrderManagementException("zip_code is not valid")
        return attr_value