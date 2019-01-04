from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="New Name"))
    app.session.logout()

def test_modify_digits(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="New Digit 22"))
    app.session.logout()
