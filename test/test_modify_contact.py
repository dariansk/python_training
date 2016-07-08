from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testcontact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = Contact(firstname="New name", lastname="Newlastname")
    modified_contact.id = contact.id
    app.contact.modify_contact_by_id(id, modified_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(modified_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
