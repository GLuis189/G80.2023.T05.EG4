from datetime import datetime
class OrderDelivered():
    def __int__(self, tracking_code):
        self.__tracking_code = tracking_code
        self.__date_delivered = datetime.utcnow().__str__()
