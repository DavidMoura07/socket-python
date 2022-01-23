class Message: 
    def __init__(self, messageCode, data, endOfData): 
        self.code = messageCode 
        self.data = data
        self.endOfData = endOfData

    def ToString(self):
        return "messageCode:%s data:%s endOfData:%s" % (self.code.name, self.data, self.endOfData)

    def __repr__(self):
        return "<messageCode:%s data:%s endOfData:%s>" % (self.code.name, self.data, self.endOfData)

    def __str__(self):
        return "messageCode:%s data:%s endOfData:%s" % (self.code.name, self.data, self.endOfData)
