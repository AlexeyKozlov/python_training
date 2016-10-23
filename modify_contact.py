from model.contact import Contact

def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New"))


def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="New"))