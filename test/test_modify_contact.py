from model.contact import Contact


def test_modify_name(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(name="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_last_name(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(lastname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
