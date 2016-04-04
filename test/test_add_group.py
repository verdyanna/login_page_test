# -*- coding: utf-8 -*-
from model.group import Group


#def test_create_group(app):
#   app.group_helper.fill_group_form(Group(name="frtyh", header="dwetreg", footer="wrehgrthb"))

#def test_assert_group(app):
#   old_groups = app.group_helper.get_group_list()
 #   app.group_helper.fill_group_form(Group(name="frtyh", header="dwetreg", footer="wrehgrthb"))
  #  new_groups = app.group_helper.get_group_list()
   # assert len(old_groups)+1 == len(new_groups)

#def test_create_mama_group(app):
 #   old_groups = app.group_helper.get_group_list()
  #  app.group_helper.fill_group_form(Group(name="mama", header="Marios", footer="moskva"))
   # new_groups = app.group_helper.get_group_list()
    #assert len(old_groups)+1 == len(new_groups)

#def test_create_empty_group(app):
#    app.group_helper.fill_group_form(Group(name="", header="", footer=""))

def test_assert_list_group(app):
    old_groups = app.group_helper.get_group_list()
    groupp = Group(name="frtyh", header="dwetreg", footer="wrehgrthb")
    app.group_helper.fill_group_form(groupp)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(groupp)

    assert sorted (old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_create_empty_group_assert(app):
    old_groups = app.group_helper.get_group_list()
    groupp = Group(name="", header="", footer="")
    app.group_helper.fill_group_form(groupp)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(groupp)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


