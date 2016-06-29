from model.contact import Contact
from random import randrange
import re


def test_all_contact_info(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testcontact", address="New York 24626", homephone="26265", workphone="997896789", mobilephone="97345632487"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_home_page = app.contact.get_contact_list()[index]
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                 [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                 [contact.email, contact.email2, contact.email3])))