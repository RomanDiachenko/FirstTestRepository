import time


def test_go_to_sent (app):
    app.tabtap.go_to_drafts()
    app.mail_operation.mail_send("romareverse9@gmail.com", "Some text")
    app.tabtap.open_set_mail()
    app.mail_operation.choose_mail()
    time.sleep(3)
