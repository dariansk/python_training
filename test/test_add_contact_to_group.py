from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="One more test"))
    group_index = random.choice(len(orm.get_group_list()))
    group = orm.get_group_list()[group_index]
    old_contacts_in_group = orm.get_contacts_in_group(group)
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Verynewtestcontact", lastname="Verynewlastname"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact.id, group_index)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)

