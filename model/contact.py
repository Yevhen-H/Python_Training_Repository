class Contact:
    def __init__(self, name=None, lastname=None, company=None, address=None, mobile=None, email=None, id=None):
        self.name = name
        self.lastname = lastname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%$:%$" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
