from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group_helper = GroupHelper(self)
        self.contact_helper = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()