# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
def is_alert_present(wd):
    try:
        wd.switch_to_alert.text
        return True
    except:
        return False

class contacts(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="kozlov", password="Kozlov30031988")
        self.open_adresses(wd)
        self.create_contact(wd, Contact(Name="Wei", Lastname="Mei", Company="weimei inc.", Title="director", City="Somerville", State="MA",
                            Zip="02145", Country="USA",
                            Phone="8573182639"))
        self.return_to_contact_page(wd)
        self.logout(wd)


    def test_add_empty_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="kozlov", password="Kozlov30031988")
        self.open_adresses(wd)
        self.create_contact(wd, Contact(Name="Empty", Lastname="Empty", Company="Empty", Title="Empty", City="", State="",
                            Zip="", Country="",
                            Phone=""))
        self.return_to_contact_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_id("anonymous_element_2").click()

    def return_to_contact_page(self, wd):
        wd.find_element_by_xpath("//div[@class='docEditButtonbar']//button[.='Save and Exit']").click()

    def create_contact(self, wd, contact):
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

    def open_adresses(self, wd):
        wd.find_element_by_link_text("Addresses").click()

    def login(self, wd, username, password):
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath("//form[@id='signinbox']//button[.=' Secure Sign In']").click()

    def open_home_page(self, wd):
        wd.get("https://www.keepandshare.com/business/logout.php?i=2683987")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
