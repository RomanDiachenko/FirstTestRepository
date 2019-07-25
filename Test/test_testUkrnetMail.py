# login, crate and send mail, switch tabs, search email and log out.
# Run file
def test_testUkrnetMail(app):
    app.open_page()
    app.session.login(login="romareverse9", password="228228228ok")
    app.mail_operation.mail_send()
    app.tabtap.tab_test()
    app.mail_operation.search_mail()
    app.session.log_out_mail()
