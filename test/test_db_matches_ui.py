
from model.contact import Contact
from timeit import timeit

def test_contact_list(app, db):
    print (timeit (lambda: app.contact.get_contact_list(), number=1))
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())
    print (timeit(lambda: map(clean, db.get_contact_list()), number=1000))
    #try:
        #assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    #except:
        #print ("Assert failed")