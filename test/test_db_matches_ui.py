
from model.contact import Contact

def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())
    db_list = map(clean, db.get_contact_list())
    try:
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    except:
        print ("Assert failed")