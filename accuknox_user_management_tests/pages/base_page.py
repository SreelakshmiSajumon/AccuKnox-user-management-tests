from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url)
    
    def wait_for_element(self, selector, timeout=10000):
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def click(self, selector):
        self.page.click(selector)
    
    def fill(self, selector, text):
        self.page.fill(selector, text)
    
    def get_text(self, selector):
        return self.page.inner_text(selector)