# -*- coding: utf-8 -*-
from model.contact_constructer import Contact_fill

def test_contact(app):
    app.contact_helper.fill_contact_form(Contact_fill(firstname="Kkkkkkk", lastname="Kkkkkkk", home="11111111111", mobile="88888888888", work="444444444"))









