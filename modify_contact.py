from model.contact import Contact

def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


