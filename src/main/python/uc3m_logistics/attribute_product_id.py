from .attribute import Attribute
from .order_management_exception import OrderManagementException

class ProductId(Attribute):
    def __init__(self, attr_value):
        self._error_message = "Invalid EAN13 code string"
        self._validation_pattern = r"^[0-9]{13}$"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value: str) -> str:
        """method vor validating a ean13 code"""
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE EAN13
        # RETURN TRUE IF THE EAN13 IS RIGHT, OR FALSE IN OTHER CASE
        checksum = 0
        code_read = -1
        result = False

        super()._validate(attr_value)

        for i, digit in enumerate(reversed(attr_value)):
            try:
                current_digit = int(digit)
            except ValueError as value_error:
                raise OrderManagementException("Invalid EAN13 code string") from value_error
            if i == 0:
                code_read = current_digit
            else:
                checksum += (current_digit) * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read != -1) and (code_read == control_digit):
            result = True
        else:
            raise OrderManagementException("Invalid EAN13 control digit")
        return attr_value