import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@id='id-l']").send_keys(login)
        driver.find_element_by_xpath("//input[@id='id-p']").send_keys(password)
        driver.find_element_by_xpath(
            "//button[@class='button button_style-main button_size-regular form__submit']").click()
        user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
        assert user_mail.text == "romareverse9@ukr.net"

    def log_out_mail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@class='login-button']").click()
        time.sleep(1)
        driver.find_element_by_id("login__logout").click()


