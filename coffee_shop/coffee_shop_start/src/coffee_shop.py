class CoffeeShop:
	
	def __init__(self,name,till):
		self.name = name
		self.till = till 
		self.drink_list = []
	
	def add_drink_to_list(self,drink):
		self.drink_list.append(drink)

	def sell_a_drink(self,customer,drink):
		customer.reduce_wallet(drink.price)
		if drink in self.drink_list:
			self.till += drink.price
	

	


# str = Customer("Stuart",200)
# geo = Customer("George",200)

# cap = Drink("Cappuchino",5)
# tea = Drink("Tea",2)
# esp = Drink("Espresso",3)

# coffee_shop = CoffeeShop("S&G",1000)

# coffee_shop.add_drink_to_list(cap)
# coffee_shop.add_drink_to_list(tea)
# coffee_shop.add_drink_to_list(esp)

# str.reduce_wallet(cap.price)
# geo.reduce_wallet(esp.price)

# coffee_shop.sell_a_drink(geo,cap)

# print(coffee_shop.till)





