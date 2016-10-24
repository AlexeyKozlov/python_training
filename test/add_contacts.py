# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contacts(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Alex", middlename="Malex", lastname="Balex", company="Talex",
                               home="1234567890", mobile="0987654321", work="1234567899",
                               email="alexe@balex"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) +1 == len(new_contacts)

def test_add_empty_contacts(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", company="",
                               home="", mobile="", work="",
                               email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
