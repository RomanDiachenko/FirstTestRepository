def test_go_to_sent (app):
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft(name="romareverse9@gmail.com", subject="Some text")
    app.tabtap.open_set_mail()
    app.mail_operation.choose_mail()