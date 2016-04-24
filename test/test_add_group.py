# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import constant as testdata

#def test_add_group_gen(app, json_groups):
#    grouup = json_groups
#    old_groups = app.group_helper.get_group_list()
#    app.group_helper.fill_group_form(grouup)
 #   assert len(old_groups) + 1 == app.group_helper.count()
 #   new_groups = app.group_helper.get_group_list()
 #   old_groups.append(grouup)
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group_gen_from_db(app,db, json_groups):
    grouup = json_groups
    old_groups = db.get_group_list()
    app.group_helper.fill_group_form(grouup)

    new_groups = db.get_group_list()
    old_groups.append(grouup)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#@pytest.mark.parametrize("group", testdata, ids=[repr (x) for x in testdata])
#def test_add_group_loop(app, group):
#        old_groups = app.group_helper.get_group_list()
#        app.group_helper.fill_group_form(group)
#        assert len(old_groups)+1 == app.group_helper.count()
 #       new_groups = app.group_helper.get_group_list()
 #       old_groups.append(group)
#        assert sorted (old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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

#def test_assert_list_group(app):
#    old_groups = app.group_helper.get_group_list()
#    groupp = Group(name="frtyh", header="dwetreg", footer="wrehgrthb")
 #   app.group_helper.fill_group_form(groupp)
#    new_groups = app.group_helper.get_group_list()
#    assert len(old_groups)+1 == len(new_groups)
#    old_groups.append(groupp)
 #   assert sorted (old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_create_empty_group_assert(app):
#    old_groups = app.group_helper.get_group_list()
#    groupp = Group(name="", header="", footer="")
#    app.group_helper.fill_group_form(groupp)
#    new_groups = app.group_helper.get_group_list()
#    assert len(old_groups)+1 == len(new_groups)
#    old_groups.append(groupp)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_xesh_list_group(app):
#    old_groups = app.group_helper.get_group_list()
#    groupp = Group(name="frtyh", header="dwetreg", footer="wrehgrthb")
#    app.group_helper.fill_group_form(groupp)
#    assert len(old_groups)+1 == app.group_helper.count()
#    new_groups = app.group_helper.get_group_list()
#    old_groups.append(groupp)
#    assert sorted (old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


