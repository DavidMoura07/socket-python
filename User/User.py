class User: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = password

    def ToString(self):
        return "username:%s password:%s" % (self.username, self.password)

    def __repr__(self):
        return "<username:%s password:%s>" % (self.username, self.password)

    def __str__(self):
        return "username:%s password:%s" % (self.username, self.password)
