from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)
    login.login("Admin", "admin123")
    admin.go_to_admin()
    admin.search_user("testuser1")
