"""Exception for the access_management module"""

class OrderManagementException(Exception):
    """Personalised exception for Order Management"""
    def __init__(self, message:str)->None:
        """Cosntructor de la clase OrderManagerException"""
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self)->str:
        """gets the message value"""
        return self.__message

    @message.setter
    def message(self,value:str)->None:
        """Setter message"""
        self.__message = value
