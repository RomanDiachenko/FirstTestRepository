def test_add_new_contact(app):
    app.new_contact.create_new_contact_button("Roman", "Diachenko", "romareverse9+1@gmail.com", "+3809379992",
                                              "Test Company", "Some test text")
    app.new_contact.delete_new_contact()