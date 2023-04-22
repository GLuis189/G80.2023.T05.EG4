from datetime import datetime
from .attribute_tracking_code import Tracking_code
class OrderDelivered():
    def __init__(self, tracking_code):
        self.__tracking_code = Tracking_code(tracking_code).value
        self.__date_delivered = datetime.utcnow().__str__()
