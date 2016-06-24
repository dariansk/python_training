from model.contact import Contact


class ContactHelper:


    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("byear", contact.birth_year)
        self.change_field_value("ayear", contact.ayear)
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
#           wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
#       if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
#          wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").click()
#       if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
#           wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
#        wd.find_element_by_name("address2").click()
#        wd.find_element_by_name("address2").clear()
#       wd.find_element_by_name("address2").send_keys(contact.address2)
#        wd.find_element_by_name("phone2").click()
#        wd.find_element_by_name("phone2").clear()
#        wd.find_element_by_name("phone2").send_keys(contact.phone2)
#       wd.find_element_by_name("notes").click()
#        wd.find_element_by_name("notes").clear()
#        wd.find_element_by_name("notes").send_keys(contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        # self.select_contact_by_index(index)
        # open modification form
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr[" + str(index + 2) + "]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text2, lastname=text1, id=id))
        return list(self.contact_cache)




