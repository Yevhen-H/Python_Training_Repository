# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Yevhen", lastname="Hurtovyi", company="Sidley", address="Chicago", mobile="7733311608",
                                       email="y.hurtovyi@yahoo.com")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_add_digits_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create_contact(Contact(name="1", lastname="2", company="3", address="4",
                                       #mobile="5", email="6"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
