import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_testUkrnetMail(app):
    app.open_page()
    app.session.login(login="romareverse9", password="228228228ok")
    app.mail_send()
    app.tab_test()
    app.search_mail()
    app.session.log_out_mail()
