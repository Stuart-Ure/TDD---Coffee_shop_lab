# from coffee_shop import CoffeeShop
class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age= age

    
    def reduce_wallet(self, amount):
        self.wallet -= amount
    
    def buy_drink(self, drink):
        if self.wallet >= drink.price:
            self.reduce_wallet(drink.price)
            return True
        else:
            return False



