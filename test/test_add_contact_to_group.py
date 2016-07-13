from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
from random import randrange


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_random_group(app):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="One more test"))
    groups = orm.get_group_list()
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="Verynewtestcontact", lastname="Verynewlastname"))
    old_contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact.id, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
    contact_in_group = False
    for item in groups:
        if item.name == group.name and contact in orm.get_contacts_in_group(item):
            contact_in_group = True
    assert contact_in_group
