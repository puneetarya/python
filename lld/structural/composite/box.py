from item import Item

class Box(Item):
    def __init__(self, contents):
        self.contents = contents
        
    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price

class Phone(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
        return self.price

class Charger(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
        return self.price

class Earphones(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
        return self.price