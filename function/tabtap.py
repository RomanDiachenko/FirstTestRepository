import time


class TabTap:

    def __init__(self, app):
        self.app = app

    # Switch tab
    def tab_test(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@id='0']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='10002']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='10001']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='10003']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='10004']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='unread']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='marked']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(
            "//a[@class='sidebar__list-link files']//span[@class='sidebar__list-link-name']").click()
        time.sleep(1)

    # Go to drafts tab
    def go_to_drafts(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@id='10002']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)

    # Open drafts tab
    def open_drafts(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='msglist__row_href']")
        time.sleep(1)

    # Open send mail
    def open_set_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@id='10001']//span[@class='sidebar__list-link-name']").click()
        time.sleep(2)

    # Open favorite
    def open_send(self):
        driver = self.app.driver
        driver.find_element_by_xpath(
            "//a[@id='10001']//span[@class='sidebar__list-link-name']").click()
        time.sleep(1)

    def set_favourite(self):
        driver = self.app.driver
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/section[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/span[1]").click()
        time.sleep(1)

    def open_marker_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@id='marked']//span[@class='sidebar__list-link-name']").click()
        time.sleep(1)
