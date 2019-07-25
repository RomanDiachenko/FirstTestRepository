import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MailOperation:

    def __init__(self, app):
        self.app = app

    def search_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@placeholder='Пошук']").send_keys("test")
        ActionChains(driver).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//a[1]//div[1]//span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(1)

    def mail_send(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("romareverse9@gmail.com")
        driver.find_element_by_xpath("//input[@name='subject']").send_keys("Some text")
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        driver.find_element_by_xpath("//button[@class='default send']").click()
        time.sleep(2)

    def write_draft(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("romareverse9@gmail.com")
        driver.find_element_by_xpath("//input[@name='subject']").send_keys("Some text")
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        driver.find_element_by_xpath("//a[@id='0']//span[@class='sidebar__list-link-name']").click()
        time.sleep(2)

    def delete_draft(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()

    def rename_drafts(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[@class='autocomplete__remove']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("romareverse9@ukr.net")
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()

    def rename_theme_drafts(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='subject']").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='subject']").send_keys("new subject")