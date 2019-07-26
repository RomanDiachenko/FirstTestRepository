import time


# modify draft name
# Run file
def test_modifydrafts_name(app):
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft(name="romareverse9@gmail.com", subject="Some text")
    app.tabtap.go_to_drafts()
    app.tabtap.open_drafts()
    app.mail_operation.rename_drafts("romareverse9@ukr.net")

# modify draft subject
def test_modifydrafts_theme(app):
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft(name="romareverse9@gmail.com", subject="Some text")
    app.tabtap.go_to_drafts()
    app.tabtap.open_drafts()
    app.mail_operation.rename_theme_drafts("new subject")


