from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, home=None,
                 mobile=None, work=None, email=None, id=None, all_phones_from_home_page=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.company=company
        self.home=home
        self.mobile=mobile
        self.work=work
        self.email=email
        self.id=id
        self.all_phones_from_home_page=all_phones_from_home_page


    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize