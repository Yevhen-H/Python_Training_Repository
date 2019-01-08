from model.contact import Contact


def test_modify_name(app):
    app.contact.create_contact(Contact(name="New name"))


def test_modify_last_name(app):
    app.contact.create_contact(Contact(lastname="New name"))
