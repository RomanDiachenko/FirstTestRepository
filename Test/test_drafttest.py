import time


# Login, write draft, delete draft and log out.
# Run file
def test_draft_test(app):
    app.tabtap.go_to_drafts()
    app.mail_operation.write_draft()
    app.tabtap.go_to_drafts()
    app.mail_operation.delete_draft()
    time.sleep(1)

