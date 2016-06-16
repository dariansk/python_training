# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ytrewq", middlename="rewq", lastname="rewq", nickname="ertyu", title="mr", company="wert", address="wertweryttwy", home="23456", mobile="236",
                               work_phone="256546", fax="255", birth_year="1234", ayear="1334", address2="46256", phone2="sfdgsdfhg", notes="sdfgh")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
#                               work_phone="", fax="", birth_year="", ayear="", address2="", phone2="", notes="")
#    app.contact.create(contact)
 #   new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
