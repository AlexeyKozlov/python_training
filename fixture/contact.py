

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_adresses()
        # init new contact
        wd.find_element_by_id("cmdItemNew").click()
        # fill contact form
        wd.find_element_by_id("fname").click()
        wd.find_element_by_id("fname").clear()
        wd.find_element_by_id("fname").send_keys(contact.Name)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.Lastname)
        wd.find_element_by_id("ABTabCompany1").click()
        wd.find_element_by_id("ABTabCompany1").clear()
        wd.find_element_by_id("ABTabCompany1").send_keys(contact.Company)
        wd.find_element_by_id("ABTabTitle1").click()
        wd.find_element_by_id("ABTabTitle1").clear()
        wd.find_element_by_id("ABTabTitle1").send_keys(contact.Title)
        if not wd.find_element_by_xpath("//select[@id='ABTabAddrType1']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@id='ABTabAddrType1']//option[1]").click()
        wd.find_element_by_id("ABTabAddr11").click()
        wd.find_element_by_id("ABTabAddr11").send_keys("")
        wd.find_element_by_id("ABTabAddr21").click()
        wd.find_element_by_id("ABTabAddr21").send_keys("")
        wd.find_element_by_id("ABTabCity1").click()
        wd.find_element_by_id("ABTabCity1").clear()
        wd.find_element_by_id("ABTabCity1").send_keys(contact.City)
        wd.find_element_by_id("ABTabState1").click()
        wd.find_element_by_id("ABTabState1").clear()
        wd.find_element_by_id("ABTabState1").send_keys(contact.State)
        wd.find_element_by_id("ABTabZip1").click()
        wd.find_element_by_id("ABTabZip1").clear()
        wd.find_element_by_id("ABTabZip1").send_keys(contact.Zip)
        wd.find_element_by_id("ABTabCountry1").click()
        wd.find_element_by_id("ABTabCountry1").clear()
        wd.find_element_by_id("ABTabCountry1").send_keys(contact.Country)
        if not wd.find_element_by_xpath("//select[@id='ABTabPhone1Type1']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@id='ABTabPhone1Type1']//option[1]").click()
        wd.find_element_by_id("ABTabPhone11").click()
        wd.find_element_by_id("ABTabPhone11").clear()
        wd.find_element_by_id("ABTabPhone11").send_keys(contact.Phone)
        wd.find_element_by_id("ABTabBirthdayDisplay1").click()
        wd.find_element_by_css_selector("button.button.gd_datepicker_dlg_display").click()
        wd.find_element_by_id("gd_datepicker_dlg_menu_year_2010").click()
        wd.find_element_by_xpath("//div[@id='gd_datepicker_dlg']/table/tbody/tr[5]/td[4]/div/div").click()
        wd.find_element_by_xpath("//div[@class='docEditButtonbar']//button[.='Save and Exit']").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_adresses()
        # select first contact
        wd.find_element_by_xpath("//div[1]/table[3]/tbody/tr/td[3]/div[3]/div[2]/table/tbody/tr[9]/td[1]/input[1]").click()
        # submit delition
        wd.find_element_by_id("cmdItemDelete").click()
        wd.find_element_by_css_selector("button.button-danger").click()
        wd.find_element_by_id("anonymous_element_2").click()


    def open_adresses(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Addresses").click()
