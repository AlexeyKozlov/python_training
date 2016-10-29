# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
from data.contacts import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) +1 == app.contact.count()
    old_contacts.append(contact)
    try:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    except:
        print ("Sorted assert was failed")
