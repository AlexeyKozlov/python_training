# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class contacts(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_contacts(self):
        success = True
        wd = self.wd
        wd.get("https://www.keepandshare.com/business/logout.php?i=2683987")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("kozlov")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("Kozlov30031988")
        wd.find_element_by_xpath("//form[@id='signinbox']//button[.=' Secure Sign In']").click()
        wd.find_element_by_link_text("Addresses").click()
        wd.find_element_by_id("cmdItemNew").click()
        wd.find_element_by_id("fname").click()
        wd.find_element_by_id("fname").clear()
        wd.find_element_by_id("fname").send_keys("Wei")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Mei")
        wd.find_element_by_id("ABTabName1").click()
        wd.find_element_by_id("ABTabName1").clear()
        wd.find_element_by_id("ABTabName1").send_keys("Weimei")
        wd.find_element_by_id("ABTabCompany1").click()
        wd.find_element_by_id("ABTabCompany1").clear()
        wd.find_element_by_id("ABTabCompany1").send_keys("weimei inc.")
        wd.find_element_by_id("ABTabTitle1").click()
        wd.find_element_by_id("ABTabTitle1").clear()
        wd.find_element_by_id("ABTabTitle1").send_keys("director")
        if not wd.find_element_by_xpath("//select[@id='ABTabAddrType1']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@id='ABTabAddrType1']//option[1]").click()
        wd.find_element_by_id("ABTabAddr11").click()
        wd.find_element_by_id("ABTabAddr11").send_keys("\\9")
        wd.find_element_by_id("ABTabAddr21").click()
        wd.find_element_by_id("ABTabAddr21").send_keys("\\9")
        wd.find_element_by_id("ABTabCity1").click()
        wd.find_element_by_id("ABTabCity1").clear()
        wd.find_element_by_id("ABTabCity1").send_keys("Somerville")
        wd.find_element_by_id("ABTabState1").click()
        wd.find_element_by_id("ABTabState1").clear()
        wd.find_element_by_id("ABTabState1").send_keys("MA")
        wd.find_element_by_id("ABTabZip1").click()
        wd.find_element_by_id("ABTabZip1").clear()
        wd.find_element_by_id("ABTabZip1").send_keys("02145")
        wd.find_element_by_id("ABTabCountry1").click()
        wd.find_element_by_id("ABTabCountry1").clear()
        wd.find_element_by_id("ABTabCountry1").send_keys("USA")
        if not wd.find_element_by_xpath("//select[@id='ABTabPhone1Type1']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@id='ABTabPhone1Type1']//option[1]").click()
        wd.find_element_by_id("ABTabPhone11").click()
        wd.find_element_by_id("ABTabPhone11").clear()
        wd.find_element_by_id("ABTabPhone11").send_keys("8573182639")
        wd.find_element_by_id("ABTabBirthdayDisplay1").click()
        wd.find_element_by_css_selector("button.button.gd_datepicker_dlg_display").click()
        wd.find_element_by_id("gd_datepicker_dlg_menu_year_2010").click()
        wd.find_element_by_xpath("//div[@id='gd_datepicker_dlg']/table/tbody/tr[5]/td[4]/div/div").click()
        wd.find_element_by_xpath("//div[@class='docEditButtonbar']//button[.='Save and Exit']").click()
        wd.find_element_by_id("anonymous_element_2").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
