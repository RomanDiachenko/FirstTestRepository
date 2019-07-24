import time


def test_draft_test(app):
    app.open_page()
    app.session.login(login="romareverse9", password="228228228ok")
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft()
    app.tabtap.go_to_drafts()
    app.mail_operation.delete_draft()
    time.sleep(1)
    app.session.log_out_mail()
