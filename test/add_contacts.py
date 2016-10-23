# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Alex", middlename="Malex", lastname="Balex", company="Talex",
                               home="1234567890", mobile="0987654321", work="1234567899",
                               email="alexe@balex"))
    app.session.logout()


def test_add_empty_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", company="",
                               home="", mobile="", work="",
                               email=""))
    app.session.logout()
