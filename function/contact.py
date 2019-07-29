import time


class Contact:

    def __init__(self, app):
        self.app = app

    def create_new_contact_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@class='contacts__head-add']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='first-name']").send_keys("Roman")
        driver.find_element_by_xpath("//input[@name='last-name']").send_keys("Diachenko")
        driver.find_element_by_xpath("//input[@name='emails']").send_keys("romareverse9+1@gmail.com")
        driver.find_element_by_xpath("//input[@name='phones']").send_keys("+3809379992")
        driver.find_element_by_xpath("//input[@name='company']").send_keys("Test Company")
        driver.find_element_by_xpath("//input[@placeholder='дд.мм.рррр']").click()
        driver.find_element_by_xpath("//td[contains(text(),'18')]").click()
        driver.find_element_by_xpath("//div[@class='modal show']//div[8]//div[2]").click()
        driver.find_element_by_xpath("//textarea[@name='notes']").send_keys("Some test text")
        driver.find_element_by_xpath("//div[@class='contacts__edit-buttons']//button[@class='default']").click()
        time.sleep(2)

    def delete_new_contact(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[contains(text(),'romareverse9+1@gmail.com')]").click()
        driver.find_element_by_xpath("//span[contains(text(),': Test Company')]").click()
        driver.find_element_by_xpath("//a[@class='link4']").click()
        driver.find_element_by_xpath(
            "//div[@class='modal show']//button[@class='default'][contains(text(),'OK')]").click()
        time.sleep(1)
