from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin()

    admin.add_user("ESS", "a", "testuser1", "Test@123")
