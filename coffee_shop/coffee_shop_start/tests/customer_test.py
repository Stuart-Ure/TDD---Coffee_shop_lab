import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.geo = Customer("George",200)
        self.coffee_shop = CoffeeShop("S&G",1000)
        self.drink= Drink("Coffee", 10)


    
    def test_customer_name(self):
        self.assertEqual("George",self.geo.name)

    def test_wallet_amount(self):
        self.assertEqual(200,self.geo.wallet)

    def test_reduce_wallet_ammout(self):
        self.geo.reduce_wallet(20)
        self.assertEqual(180,self.geo.wallet)

    def buy_drink(self):
        self.assertEqual(self.drink.name,"Coff")