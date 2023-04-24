"""MODULE: order_request. Contains the order request class"""
import hashlib
import json
from datetime import datetime
from uc3m_logistics.data.data_attr.attribute_phone_number import PhoneNumber
from uc3m_logistics.data.data_attr.attribute_address import Address
from uc3m_logistics.data.data_attr.attribute_order_type import OrderType
from uc3m_logistics.data.data_attr.attribute_zip_code import ZipCode
from uc3m_logistics.data.data_attr.attribute_product_id import ProductId
from uc3m_logistics.store.json_store_order import JsonOrderStore


class OrderRequest:
    """Class representing the register of the order in the system"""
    #pylint: disable=too-many-arguments
    def __init__( self, product_id:str, order_type:str,
                  delivery_address:str, phone_number:str, zip_code:str)->None:
        """Constructor de la clase OrderRequest"""
        self.__product_id = ProductId(product_id).value
        self.__delivery_address = Address(delivery_address).value
        self.__order_type = OrderType(order_type).value
        self.__phone_number = PhoneNumber(phone_number).value
        self.__zip_code = ZipCode(zip_code).value
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)
        self.__order_id = hashlib.md5(self.__str__().encode()).hexdigest()



    def __str__(self):
        """Función str"""
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def delivery_address( self )->str:
        """Property representing the address where the product
        must be delivered"""
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address( self, value:str )->None:
        """Setter delivery address"""
        self.__delivery_address = value

    @property
    def order_type( self )->str:
        """Property representing the type of order: REGULAR or PREMIUM"""
        return self.__order_type
    @order_type.setter
    def order_type( self, value:str )->None:
        """Setter order type"""
        self.__order_type = value

    @property
    def phone_number( self )->str:
        """Property representing the clients's phone number"""
        return self.__phone_number
    @phone_number.setter
    def phone_number( self, value:str )->None:
        """Setter phone number"""
        self.__phone_number = value

    @property
    def product_id( self )->str:
        """Property representing the products  EAN13 code"""
        return self.__product_id
    @product_id.setter
    def product_id( self, value:str )->None:
        """Setter the product_id"""
        self.__product_id = value

    @property
    def time_stamp(self)->float:
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def order_id( self )->str:
        """Returns the md5 signature"""
        return self.__order_id

    @property
    def zip_code( self )->str:
        """Returns the order's zip_code"""
        return self.__zip_code

    def crear_json(self)->None:
        """Crear el json"""
        my_store = JsonOrderStore()
        my_store.add_item(self)
