from model.contact import Contact


def modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New"))
    app.session.logout()


def modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New"))
    app.session.logout()