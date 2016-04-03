# -*- coding: utf-8 -*-
from model.group import Group

#def test_create_group(app):
#   app.group_helper.fill_group_form(Group(name="frtyh", header="dwetreg", footer="wrehgrthb"))

def test_assert_group(app):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.fill_group_form(Group(name="frtyh", header="dwetreg", footer="wrehgrthb"))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

def test_create_mama_group(app):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.fill_group_form(Group(name="mama", header="Marios", footer="moskva"))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

def test_create_empty_group(app):
    app.group_helper.fill_group_form(Group(name="", header="", footer=""))


