class NewOrder: 
    def __init__(self, productName, quantity): 
        self.productName = productName
        self.quantity = int(quantity)

    def ToString(self):
        return "product:%s quantity:%s" % (self.productName, self.quantity)

    def __repr__(self):
        return "<product:%s quantity:%s>" % (self.productName, self.quantity)

    def __str__(self):
        return "product:%s quantity:%s" % (self.productName, self.quantity)
