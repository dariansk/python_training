from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
from random import randrange


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    #if len(orm.get_group_list()) == 0:
    #    app.group.create(Group(name="One more test"))
    #group_index = randrange(0, len(orm.get_group_list()) - 1)
    #group = app.group.get_group_index_list()[group_index]
    old_contacts_in_group = orm.get_contacts_in_group(Group(id="43"))
    if len(orm.get_contacts_not_in_group(Group(id="43"))) == 0:
        app.contact.create(Contact(firstname="Verynewtestcontact", lastname="Verynewlastname"))
    contact = random.choice(orm.get_contacts_not_in_group(Group(id="43")))
    app.contact.add_contact_to_group(contact.id)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id="43"))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)


#def test_add_contact_to_random_group(app):
#    if len(orm.get_group_list()) == 0:
#        app.group.create(Group(name="One more test"))
#    group_index = randrange(0, len(orm.get_group_list()) - 1)
#    for item in app.group.get_group_index_list():
#        global group
#        group = []
#        if item.index == group_index:
#            group = item
#        return group
#    old_contacts_in_group = orm.get_contacts_in_group(group)
#    if len(orm.get_contacts_not_in_group(group)) == 0:
#        app.contact.create(Contact(firstname="Verynewtestcontact", lastname="Verynewlastname"))
#    contact = random.choice(orm.get_contacts_not_in_group(group))
#    app.contact.add_contact_to_group(contact.id, group_index)
#    new_contacts_in_group = orm.get_contacts_in_group(group)
#    old_contacts_in_group.append(contact)
#    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
