from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, id=None,
                 all_phones_from_home_page=None, email=None, company=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.email=email
        self.middlename=middlename
        self.company=company


    def __repr__(self):
        return "%s:%s %s %s" % (self.id, self.firstname, self.middlename, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize