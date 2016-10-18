# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




def test_contacts(app):
    app.login(username="kozlov", password="Kozlov30031988")
    app.create_contact(Contact(Name="Wei", Lastname="Mei", Company="weimei inc.", Title="director", City="Somerville", State="MA",
                                    Zip="02145", Country="USA",
                                    Phone="8573182639"))
    app.logout()

def test_add_empty_contacts(app):
    app.login(username="kozlov", password="Kozlov30031988")
    app.create_contact(Contact(Name="Empty", Lastname="Empty", Company="Empty", Title="Empty", City="", State="",
                                    Zip="", Country="",
                                    Phone=""))
    app.logout()

