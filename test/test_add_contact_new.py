# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="Yevhen", lastname="Hurtovyi", company="Sidley", address="Chicago", mobile="7733311608",
                    email="y.hurtovyi@yahoo.com"))
    app.session.logout()


def test_add_digits_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="1", lastname="2", company="3", address="4",
                                    mobile="5", email="6"))
    app.session.logout()
