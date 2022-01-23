class Order: 
    def __init__(self, customer, product, price, quantity, datetime): 
        self.customer = customer 
        self.product = product
        self.price = price
        self.quantity = quantity
        self.datetime = datetime

    def ToString(self):
        return "customer:%s product:%s price:%s quantity:%s datetime:%s" % (self.customer, self.product, self.price, self.quantity, self.datetime)

    def __repr__(self):
        return "<customer:%s product:%s price:%s quantity:%s datetime:%s>" % (self.customer, self.product, self.price, self.quantity, self.datetime)

    def __str__(self):
        return "customer:%s product:%s price:%s quantity:%s datetime:%s" % (self.customer, self.product, self.price, self.quantity, self.datetime)
