from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testcontact"))
    app.contact.modify_first_contact(Contact(firstname="New name"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="testcontact"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

