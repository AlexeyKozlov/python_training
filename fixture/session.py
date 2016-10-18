


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath("//form[@id='signinbox']//button[.=' Secure Sign In']").click()

    def logout(self):
        wd = self.app.wd
        self.app.return_to_contact_page()
        wd.find_element_by_id("anonymous_element_2").click()
