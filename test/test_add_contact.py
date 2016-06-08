# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="ytrewq", middlename="rewq", lastname="rewq", nickname="ertyu", title="mr", company="wert", address="wertweryttwy", home="23456", mobile="236",
                               work_phone="256546", fax="255", birth_year="1234", ayear="1334", address2="46256", phone2="sfdgsdfhg", notes="sdfgh"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               work_phone="", fax="", birth_year="", ayear="", address2="", phone2="", notes=""))
