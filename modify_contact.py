from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New"))
    app.session.logout()