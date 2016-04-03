# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group_helper.count() == 0:
        app.group_helper.fill_group_form(Group(name="misha"))
    app.group_helper.delete_first_group()


