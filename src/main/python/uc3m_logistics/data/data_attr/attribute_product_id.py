"""MODULES"""
from uc3m_logistics.data.data_attr.attribute import Attribute
from uc3m_logistics.exception.order_management_exception import OrderManagementException

class ProductId(Attribute):
    """Clase hija,atributo ProductId"""
    __ERROR = "Invalid EAN13 code string"
    __ERROR_DIGIT = "Invalid EAN13 control digit"
    __PATTERN = r"^[0-9]{13}$"
    def __init__(self, attr_value:str)->None:
        """Constructor"""
        super().__init__()
        self._error_message = self.__ERROR
        self._validation_pattern = self.__PATTERN
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value: str) -> str:
        """method vor validating a ean13 code"""
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE EAN13
        # RETURN TRUE IF THE EAN13 IS RIGHT, OR FALSE IN OTHER CASE
        checksum = 0
        code_read = -1

        super()._validate(attr_value)

        for i, digit in enumerate(reversed(attr_value)):
            try:
                current_digit = int(digit)
            except ValueError as value_error:
                raise OrderManagementException(self.__ERROR) from value_error
            if i == 0:
                code_read = current_digit
            else:
                checksum += (current_digit) * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read == -1) or (code_read != control_digit):
            raise OrderManagementException(self.__ERROR_DIGIT)
        return attr_value
