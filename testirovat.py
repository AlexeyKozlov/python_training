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

class testirovat(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testirovat(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        if wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").get_attribute("value") != "Login":
            success = False
            print("verifyElementValue failed")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input")).perform()
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("qwddsa")
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
