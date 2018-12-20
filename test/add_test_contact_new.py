# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application_contact import Application
import pytest


@pytest.fixture
def app (request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.create_contact(
            Contact(name="Yevhen", lastname="Hurtovyi", company="Sidley", address="Chicago", mobile="7733311608",
                    email="y.hurtovyi@yahoo.com"))
    app.session_contact.logout()


def test_add_digits_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="1", lastname="2", company="3", address="4",
                                    mobile="5", email="6"))
    app.session_contact.logout()
