# -*- coding: utf-8 -*-
from model.contact_constructer import Contact_fill

def test_delete_first_contact(app):
    if app.contact_helper.count_contact() == 0:
        app.contact_helper.fill_contact_form(Contact_fill(firstname="Kkkkkkk", middlename="Kkkkkkk", lastname="Kkkkkkk",
                                                          address="Kkkkkkk", home="11111111111"))
    app.contact_helper.delete_first_contact()



