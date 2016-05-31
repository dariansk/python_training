from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="3737675676", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               work_phone="", fax="", birth_year="", ayear="", address2="", phone2="", notes=""))
    app.session.logout()
