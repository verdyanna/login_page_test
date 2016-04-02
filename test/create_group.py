# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_group(app):

    app.session.login(username="admin", password="secret")
    app.group_helper.fill_group_form(Group(name="frtyh", header="dwetreg", footer="wrehgrthb"))
    app.session.logout()

def test_create_mama_group(app):

    app.session.login(username="admin", password ="secret")
    app.group_helper.fill_group_form( Group(name="mama", header="Marios", footer="moskva"))
    app.session.logout()

def test_create_empty_group(app):

    app.session.login(username="admin", password ="secret")
    app.group_helper.fill_group_form(Group(name="", header="", footer=""))
    app.session.logout()


