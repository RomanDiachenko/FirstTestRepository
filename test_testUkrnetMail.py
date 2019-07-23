import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_testUkrnetMail(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")
        self.driver.maximize_window()
        self.login(driver, login="romareverse9", password="228228228ok")
        self.mail_send(driver)
        self.tab_test(driver)
        self.search_mail(driver)
        self.log_out_mail(driver)

    def search_mail(self, driver):
        driver.find_element_by_xpath("//input[@placeholder='Пошук']").send_keys("test")
        ActionChains(driver).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("//a[1]//div[1]//span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='controls-link remove']").click()
        time.sleep(1)

    def tab_test(self, driver):
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

    def log_out_mail(self, driver):
        driver.find_element_by_xpath("//a[@class='login-button']").click()
        driver.find_element_by_id("login__logout").click()

    def login(self, driver, login, password):
        driver.find_element_by_id("id-l").send_keys(login)
        driver.find_element_by_id("id-p").send_keys(password)
        driver.find_element_by_xpath(
            "//button[@class='button button_style-main button_size-regular form__submit']").click()
        user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
        assert user_mail.text == "romareverse9@ukr.net"

    def mail_send(self, driver):
        driver.find_element_by_xpath("//button[@class='default compose']").click()
        driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("romareverse9@gmail.com")
        driver.find_element_by_xpath("//input[@name='subject']").send_keys("Some text")
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")
        driver.find_element_by_xpath("//button[@class='default send']").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

        if __name__ == "__main__":
            unittest.main()
