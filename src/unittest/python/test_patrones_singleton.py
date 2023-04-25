"""MODULES"""
from unittest import TestCase
from uc3m_logistics import OrderManager
from uc3m_logistics.store.json_store_order import JsonOrderStore
from uc3m_logistics.store.json_store_delivered import JsonDeliverStore
from uc3m_logistics.store.json_store_shipments import JsonShipmentsStore

class TestDeliverProduct(TestCase):
    """Test Singleton"""
    def test_singleton_order_manager(self):
        """Test para la clase OrderManager"""
        object1 = OrderManager()
        object2 = OrderManager()
        self.assertEqual(object1, object2)
    def test_singleton_json_store_order(self):
        """Test para la clase JsonOrderStore"""
        object1 = JsonOrderStore()
        object2 = JsonOrderStore()
        self.assertEqual(object1, object2)

    def test_singleton_json_shipments_order(self):
        """Test para la clase JsonShipmentsStore"""
        object1 = JsonShipmentsStore()
        object2 = JsonShipmentsStore()
        self.assertEqual(object1, object2)

    def test_singleton_json_deliver_order(self):
        """Test para la clase JsonDeliverStore"""
        object1 = JsonDeliverStore()
        object2 = JsonDeliverStore()
        self.assertEqual(object1, object2)
