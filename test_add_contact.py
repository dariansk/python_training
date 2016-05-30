# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application2 import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="ytrewq", middlename="rewq", lastname="rewq", nickname="ertyu", title="mr", company="wert", address="wertweryttwy", home="23456", mobile="236",
                                work_phone="256546", fax="255", birth_year="1234", ayear="1334", address2="46256", phone2="sfdgsdfhg", notes="sdfgh"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                                work_phone="", fax="", birth_year="", ayear="", address2="", phone2="", notes=""))
    app.logout()
