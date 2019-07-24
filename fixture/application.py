from selenium import webdriver

from function.MailOperation import MailOperation
from function.session import SessionHelper
from function.tabtap import TabTap


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.session = SessionHelper(self)
        self.tabtap = TabTap(self)
        self.mail_operation = MailOperation(self)

    def open_page(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")

    def destroy(self):
        self.driver.quit()
