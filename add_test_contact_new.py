# -*- coding: utf-8 -*-
from contact import Contact
from application_contact import Application_Contact
import pytest

@pytest.fixture
def app (request):
    fixture = Application_Contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
            Contact(name="Yevhen", lastname="Hurtovyi", company="Sidley", address="Chicago", mobile="7733311608",
                    email="y.hurtovyi@yahoo.com"))
    app.logout()


def test_add_digits_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="1", lastname="2", company="3", address="4",
                                    mobile="5", email="6"))
    app.logout()
