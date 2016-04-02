# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact_constructer import Contact_fill


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact_helper.fill_contact_form(Contact_fill(firstname="Salamina", lastname="Marik", address="Kasnofirsk",
                               home_phome="898654433", mobile_phone="769403", work_phone="859335", fax="3y48505-",
                               email_na="janes.fiddler@mail.ru"))
    app.session.logout()








