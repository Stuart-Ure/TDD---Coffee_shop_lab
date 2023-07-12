import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.geo = Customer("George",200)

        self.tea = Drink("Tea",2)

        self.coffee_shop = CoffeeShop("S&G",1000)

    def test_coffee_shop_has_name(self):
        self.assertEqual("S&G", self.coffee_shop.name)

    def test_sell_drink(self):
        self.coffee_shop.till += self.tea.price
        self.assertEqual(self.coffee_shop.till,1002)

    @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        pass