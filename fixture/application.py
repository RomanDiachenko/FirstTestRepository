import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.session = SessionHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")

    def search_mail(self):
        driver = self.driver
        driver.find_element_by_xpath("//input[@placeholder='Пошук']").send_keys("test")
        ActionChains(driver).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//a[1]//div[1]//span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(1)

    def tab_test(self):
        driver = self.driver
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



    def mail_send(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("romareverse9@gmail.com")
        driver.find_element_by_xpath("//input[@name='subject']").send_keys("Some text")
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        driver.find_element_by_xpath("//button[@class='default send']").click()
        time.sleep(2)

    def destroy(self):
        self.driver.quit()
