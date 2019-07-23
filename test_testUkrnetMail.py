import time
import unittest
from selenium import webdriver


# импорт библиотек


class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)

    # создаём класс, указываем путь к драйверу и выставляем timeout

    def test_testUkrnetMail(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")
        self.driver.maximize_window()
        self.login(driver, login="romareverse9", password="228228228ok")
        self.validate_login(driver)
        self.mail_send(driver)
        self.Fiend_addressee(driver)
        self.enter_theme(driver)
        self.field_text(driver)
        self.send_message(driver)
        self.log_out_mail(driver)

    def send_message(self, driver):
        send_message_button = driver.find_element_by_xpath("//button[@class='default send']")
        send_message_button.click()
        time.sleep(5)

    def field_text(self, driver):
        driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % "some text from this test case")

    def enter_theme(self, driver):
        theme_field = driver.find_element_by_xpath("//input[@name='subject']")
        theme_field.send_keys("Some text")

    def Fiend_addressee(self, driver):
        addressee_mail = driver.find_element_by_xpath("//input[@name='toFieldInput']")
        addressee_mail.send_keys("romareverse9@gmail.com")

    def log_out_mail(self, driver):
        drop_bar = driver.find_element_by_xpath("//a[@class='login-button']")
        drop_bar.click()
        log_out = driver.find_element_by_id("login__logout")
        log_out.click()

    def validate_login(self, driver):
        user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
        assert user_mail.text == "romareverse9@ukr.net"

    def login(self, driver, login, password):
        login_field = driver.find_element_by_id("id-l")
        login_field.send_keys(login)
        password_field = driver.find_element_by_id("id-p")
        password_field.send_keys(password)
        button_login = driver.find_element_by_xpath(
            "//button[@class='button button_style-main button_size-regular form__submit']")
        button_login.click()

    def mail_send(self, driver):
        send_mail_button = driver.find_element_by_xpath("//button[@class='default compose']")
        send_mail_button.click()

    def tearDown(self):
        self.driver.quit()

        if __name__ == "__main__":
            unittest.main()
