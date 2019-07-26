# login, crate and send mail, switch tabs, search email and log out.
# Run file
def test_testUkrnetMail(app):
    app.tabtap.go_to_drafts()
    app.mail_operation.mail_send("romareverse9@gmail.com", "Some text")
    app.tabtap.tab_test()
    app.mail_operation.search_mail()

