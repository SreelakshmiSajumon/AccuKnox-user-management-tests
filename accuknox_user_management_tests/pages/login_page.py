from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "button:has-text('Login')"
    
    def login(self, username, password):
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.login_button)