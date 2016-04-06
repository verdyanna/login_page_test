from sys import maxsize

class Contact_fill:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None,
                 address=None, home=None, mobile=None, work=None, fax=None, phone2=None, email=None):

        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.fax = fax
        self.email = email

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
