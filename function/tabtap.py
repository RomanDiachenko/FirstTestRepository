import time


class TabTap:

    def __init__(self, app):
        self.app = app

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

    def go_to_drafts(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@id='10002']//span[@class='sidebar__list-link-name']").click()
        time.sleep(0.5)
