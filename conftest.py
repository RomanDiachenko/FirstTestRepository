import pytest

from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.open_page()
        fixture.session.login(login="romareverse9", password="228228228ok")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.open_page()
            fixture.session.login(login="romareverse9", password="228228228ok")

    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.log_out_mail()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
