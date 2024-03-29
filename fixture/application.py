from selenium import webdriver

from function.MailOperation import MailOperation
from function.session import SessionHelper
from function.contact import Contact
from function.tabtap import TabTap
from selenium.common.exceptions import NoSuchElementException


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.session = SessionHelper(self)
        self.tabtap = TabTap(self)
        self.mail_operation = MailOperation(self)
        self.new_contact = Contact(self)

    def check_exists_by_xpath(xpath):
        driver = xpath.driver
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def open_page(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")

    def destroy(self):
        self.driver.quit()
