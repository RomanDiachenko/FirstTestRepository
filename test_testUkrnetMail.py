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
        self.log_out_mail(driver)

    def log_out_mail(self, driver):
        drop_bar = driver.find_element_by_css_selector(
            "body.theme-white:nth-child(2) div.contacts-shown:nth-child(1) header.header.animate div.header__login div.login div.login__login-button a.login-button > p.login-button__user")
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
        button_login = driver.find_element_by_css_selector(
            'div.root:nth-child(1) div.app main.app__main form.form > button.button.button_style-main.button_size-regular.form__submit:nth-child(4)')
        button_login.click()

    def mail_send(self, driver):
        send_mail_button = driver.find_element_by_css_selector(
            "body.theme-white:nth-child(2) div.contacts-shown:nth-child(1) div:nth-child(2) aside.sidebar > button.default.compose")
        send_mail_button.click()

    def tearDown(self):
        self.driver.quit()

        if __name__ == "__main__":
            unittest.main()
