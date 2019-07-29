import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MailOperation:

    def __init__(self, app):
        self.app = app

    # Search and choose first mail
    def search_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@placeholder='Пошук']").send_keys("test")
        ActionChains(driver).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//a[1]//div[1]//span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(1)

    # Create and send mail
    def mail_send(self, name, subject):
        driver = self.app.driver
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys(name)
        driver.find_element_by_xpath("//input[@name='subject']").send_keys(subject)
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='default send']").click()
        time.sleep(2)

    # Create draft
    def write_draft(self, name, subject):
        driver = self.app.driver
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys(name)
        driver.find_element_by_xpath("//input[@name='subject']").send_keys(subject)
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        driver.find_element_by_xpath("//a[@id='0']//span[@class='sidebar__list-link-name']").click()
        time.sleep(2)

    # Delete drafts
    def delete_draft(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()

    # Change mail addressee
    def rename_drafts(self, new_name):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[@class='autocomplete__remove']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys(new_name)
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()

    # Change mail subject
    def rename_theme_drafts(self, new_subject):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='subject']").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='subject']").send_keys(new_subject)

    def choose_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//tr[@id='msg15641224113199512172']//input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link more']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='link2 showCorrespondence']").click()
        time.sleep(1)
        driver.find_element_by_css_selector(
            "body.theme-white:nth-child(2) div.contacts-shown:nth-child(1) div.animate div.msglist div.screen__content table.noselect tbody:nth-child(3) tr.msglist__row.icon0.ui-draggable:nth-child(1) td.msglist__row-check label.checkbox.noselect > input:nth-child(1)").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(1)

    def set_favourite_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//span[@class='msglist__row-address-wrap']").click()
        time.sleep(1)

    def delete_favourite_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(2)

