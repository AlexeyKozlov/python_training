# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Alex", middlename="Malex", lastname="Balex", company="Talex",
                        home="1234567890", mobile="0987654321", work="1234567899",
                        email="alexe@balex"))
    app.logout()


def test_add_empty_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", company="",
                        home="", mobile="", work="",
                        email=""))
    app.logout()
