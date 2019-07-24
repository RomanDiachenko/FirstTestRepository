
def __init__(self, email):
    self.email = email


def test_testUkrnetMail(self):
    driver = self.driver
    driver.get("https://mail.ukr.net/desktop/login")
    self.driver.maximize_window()

    self.login(login="romareverse9", password="228228228ok")
    self.mail_send()
    self.tab_test()
    self.search_mail()
    self.log_out_mail()


class Person:

    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def display_info(self):
        print("Привет, меня зовут", self.name)


person1 = Person("Tom")
person1.display_info()  # Привет, меня зовут Tom
person2 = Person("Sam")
person2.display_info()  # Привет, меня зовут Sam


person1 = emai