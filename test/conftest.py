# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
        request.addfinalizer(fin)
    request.addfinalizer(fixture.destroy)
    return fixture
