def test_delete_user(login_page, admin_page, page, user_data):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page.login("Admin", "admin123")
    
    admin_page.navigate_to_admin_module()
    
    admin_page.delete_user(user_data["username"])
    