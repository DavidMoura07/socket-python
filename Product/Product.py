class Product: 
    def __init__(self, name, price, stockQuantity): 
        self.name = name 
        self.price = price
        self.stockQuantity = stockQuantity
    
    def UpdateStock(self, stockQuantity):
        self.stockQuantity = stockQuantity
        if (self.stockQuantity < 0):
            self.stockQuantity = 0
        return self.stockQuantity

    def IncreaseStock(self, quantity):
        self.stockQuantity += quantity
        return self.stockQuantity

    def DecreaseStock(self, quantity):
        self.stockQuantity -= quantity
        if (self.stockQuantity < 0):
            self.stockQuantity = 0
        return self.stockQuantity

    def ChangePrice(self, newPrice):
        self.price = newPrice
        if (self.price < 0):
            self.price = 0
        return self.price

    def ToString(self):
        return "Name:%s Price:%s Stock_Quantity:%s" % (self.name, self.price, self.stockQuantity)

    def __repr__(self):
        return "<name:%s price:%s stockQuantity:%s>" % (self.name, self.price, self.stockQuantity)

    def __str__(self):
        return "Name:%s Price:%s Stock_Quantity:%s" % (self.name, self.price, self.stockQuantity)
