from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
from random import randrange


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="One more test"))
    # precondition: there is a group with contacts in it
    no_contacts_in_groups = True
    groups = orm.get_group_list()
    for item in groups:
        if len(orm.get_contacts_in_group(item)) > 0:
            no_contacts_in_groups = False
            break
    if no_contacts_in_groups: 
        app.contact.add_contact_to_group(Contact(firstname="New contact", lastname="New lastname"), groups[0])
    # select group and contact
    group = None
    contact = None
    for item1 in orm.get_group_list():
        contacts_in_group = orm.get_contacts_in_group(item1)
        if len(contacts_in_group) > 0:
            group = item1
            contact = contacts_in_group[0]
            break
    app.contact.delete_from_group(contact.id, group)
    # check if contact is deleted from group
    contact_is_deleted = True
    for i in orm.get_group_list():
        if contact in orm.get_contacts_in_group(i):
            contact_is_deleted = False
            break
    assert contact_is_deleted

