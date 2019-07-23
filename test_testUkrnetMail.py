from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def testUkrnetMail(app):
    app.login(login="romareverse9", password="228228228ok")
    app.mail_send()
    app.tab_test()
    app.search_mail()
    app.log_out_mail()