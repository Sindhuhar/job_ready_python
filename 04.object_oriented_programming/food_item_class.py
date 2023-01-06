class food_item:
    def  __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: Rs." + str(self.price) + "\n"
    def get_price(self):
        return self.price

class drink(food_item):
    def __init__(self,name,size,price):
        super(drink, self).__init__(name,price)
        self.size= size
    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "oz"
        return s