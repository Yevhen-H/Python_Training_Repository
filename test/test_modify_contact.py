from model.contact import Contact


def test_modify_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="New name")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_lastname(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create_contact(Contact(lastname="New lastname"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
