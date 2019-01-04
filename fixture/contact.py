class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text.name is not None:
            wd.find_element_by_link_text("add new").click()
            wd.find_element_by_name("field_name").click()
            wd.find_element_by_name("field_name").clear()
            wd.find_element_by_name("field_name").send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first group
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.return_to_the_home()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        #open
        wd.find_element_by_title("Edit").click()
        #fill
        self.fill_contact_form(new_contact_data)
        #submit
        wd.find_element_by_name("update").click()
        self.return_to_the_home()

    def return_to_the_home(self):
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
