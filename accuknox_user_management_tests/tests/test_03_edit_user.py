def test_edit_existing_user_role(login_page, admin_page, page, existing_test_user, edited_user_data):
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    
    admin_page.navigate_to_admin_module()
    
    admin_page.edit_user_role(existing_test_user["username"], edited_user_data["role"])
    
    admin_page.search_user(existing_test_user["username"])
    current_role = admin_page.get_user_role(existing_test_user["username"])
    assert current_role == edited_user_data["role"]