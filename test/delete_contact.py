# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import  unittest



class delete_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_delete_contact(self):

        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("home").click()
        if not wd.find_element_by_id("4").is_selected():
            wd.find_element_by_id("4").click()
        if not wd.find_element_by_id("2").is_selected():
            wd.find_element_by_id("2").click()
        if wd.find_element_by_id("4").is_selected():
            wd.find_element_by_id("4").click()
        if not wd.find_element_by_id("1").is_selected():
            wd.find_element_by_id("1").click()
        if wd.find_element_by_id("2").is_selected():
            wd.find_element_by_id("2").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
