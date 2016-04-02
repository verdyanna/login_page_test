# -*- coding: utf-8 -*-
from model.contact_constructer import Contact_fill

def test_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact_helper.fill_contact_form(Contact_fill(firstname="Kkkkkkk", middlename="Kkkkkkk", lastname="Kkkkkkk", address="Kkkkkkk", home="11111111111", mobile="88888888888", work="444444444", fax="66666666", email=""))
    app.session.logout()








