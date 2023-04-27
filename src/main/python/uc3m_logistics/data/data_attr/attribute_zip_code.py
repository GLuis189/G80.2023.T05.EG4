"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class ZipCode(Attribute):
    """Clase hija, atributo ZipCode"""
    __ERROR1 = "zip_code format is not valid"
    __ERROR2 = "zip_code is not valid"
    __PATTERN = r"[0-9]{5}"
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = self.__ERROR1
        self._validation_pattern = self.__PATTERN
        self._attr_value = self.validate_zip_code(attr_value)

    def validate_zip_code(self, attr_value:str)->str:
        """Validar zip_code"""
        super()._validate(attr_value)
        if (int(attr_value) > 52999 or int(attr_value) < 1000):
            raise OrderManagementException(self.__ERROR2)
        return attr_value
