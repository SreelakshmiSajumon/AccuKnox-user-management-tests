def test_add_user(login_page, admin_page, page, user_data):
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page.login("Admin", "admin123")
    
    admin_page.navigate_to_admin_module()
    
    admin_page.add_user(user_data)
    
    admin_page.search_user(user_data["username"])
    assert admin_page.is_user_found(user_data["username"]), "User was not added successfully"