from model.contact import Contact

def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.modify_first_contact(Contact(firstname="New"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



