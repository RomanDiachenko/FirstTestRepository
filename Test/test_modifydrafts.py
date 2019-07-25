import time


# modify draft name
# Run file
def test_modifydrafts_name(app):
    app.open_page()
    app.session.login(login="romareverse9", password="228228228ok")
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft()
    app.tabtap.go_to_drafts()
    app.tabtap.open_drafts()
    app.mail_operation.rename_drafts()
    time.sleep(1)
    app.session.log_out_mail()

# modify draft subject
def test_modifydrafts_theme(app):
    app.open_page()
    app.session.login(login="romareverse9", password="228228228ok")
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft()
    app.tabtap.go_to_drafts()
    app.tabtap.open_drafts()
    app.mail_operation.rename_theme_drafts()
    time.sleep(1)
    app.session.log_out_mail()

