import mysql.connector
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, home, mobile, work from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, home, mobile, work) = row
                list.append(Contact(id=str(id), firstname = firstname,middlename=middlename,lastname = lastname, homephone = home,
                        mobilephone = mobile, workphone = work))
        finally:
            cursor.close()
            return list

    def destroy(self):
        self.connection.close()

