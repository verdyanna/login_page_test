# -*- coding: utf-8 -*-
from model.group import Group
#from random import randrange
import random

#def test_delete_first_group(app):
#    if app.group_helper.count() == 0:
#        app.group_helper.fill_group_form(Group(name="misha"))
#    app.group_helper.delete_first_group()
 #   new_groups = app.group_helper.get_group_list()
 #   assert len(old_groups)-1 == len(new_groups)
#    old_groups[0:1] = []
 #   assert old_groups == new_groups

#def test_delete_some_group(app):
 #   if app.group_helper.count() == 0:
#        app.group_helper.fill_group_form(Group(name="misha", header="HHHhhh"))
 #   old_groups = app.group_helper.get_group_list()
#    index = randrange(len(old_groups))
#    app.group_helper.delete_group_by_index(index)
#    new_groups = app.group_helper.get_group_list()
 #   assert len(old_groups)-1 == len(new_groups)
#    old_groups[index:index+1] = []
#    assert old_groups == new_groups

def test_delete_some_group(app,db, check_web):
    if len(db.get_group_list()) == 0:
        app.group_helper.fill_group_form(Group(name="krispi"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group_helper.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_web:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)

