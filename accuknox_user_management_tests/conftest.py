import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def admin_page(page):
    return AdminPage(page)

@pytest.fixture
def user_data():
    return {
        "employee_name": "a",  
        "username": "testuser1",  
        "password": "P@ssw0rd123",
        "role": "ESS",
        "status": "Enabled"
    }

@pytest.fixture
def existing_test_user():
    return {
        "username": "testuser1",  
        "password": "P@ssw0rd123" 
    }

@pytest.fixture
def edited_user_data():
    return {
        "role": "Admin",  
    }