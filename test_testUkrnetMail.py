import unittest
from selenium import webdriver


class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_testUkrnetMail(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")
        login_field = driver.find_element_by_id("id-l")
        login_field.send_keys("romareverse9")
        password_field = driver.find_element_by_id("id-p")
        password_field.send_keys("228228228ok")
        

        if __name__ == "__main__":
            unittest.main()
