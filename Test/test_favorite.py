def test_favorite(app):
    app.tabtap.open_send()
    app.tabtap.set_favourite()
    app.tabtap.open_marker_mail()
    app.mail_operation.set_favourite_mail()
    app.mail_operation.delete_favourite_mail()

