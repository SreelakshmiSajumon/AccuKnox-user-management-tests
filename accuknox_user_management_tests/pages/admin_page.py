import time
from playwright.sync_api import expect
from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.add_button = page.get_by_role("button", name="Add")
        self.user_role = page.locator(".oxd-select-text").nth(0)
        self.employee_name = page.get_by_placeholder("Type for hints...")
        self.status = page.locator(".oxd-select-text").nth(1)
        self.username = page.locator("input[autocomplete='off']").nth(1)
        self.password = page.locator("input[type='password']").nth(0)
        self.confirm_password = page.locator("input[type='password']").nth(1)
        self.save_button = page.get_by_role("button", name="Save")
        self.search_input = page.locator("input[placeholder='Search']")
        self.search_button = page.get_by_role("button", name="Search")
        self.edit_button = page.get_by_role("button", name="Edit")
        self.delete_button = page.get_by_role("button", name="Delete Selected")
        self.confirm_delete = page.get_by_role("button", name="Yes, Delete")

    def go_to_admin(self):
        self.admin_menu.click()

    def add_user(self, role, emp_search_term, uname, pwd):
        self.add_button.click()
        self.page.wait_for_selector("text=Add User")

        
        self.user_role.click()
        self.page.get_by_role("option", name=role).click()

        
        self.employee_name.fill(emp_search_term)

        
        time.sleep(2)  

        
        suggestion = self.page.locator("div.oxd-autocomplete-dropdown > div").first

        
        expect(suggestion).to_be_visible(timeout=5000)

        
        suggestion.click()

        
        self.status.click()
        self.page.get_by_role("option", name="Enabled").click()

        
        self.username.fill(uname)
        self.password.fill(pwd)
        self.confirm_password.fill(pwd)

        
        self.save_button.click()

        
        self.page.wait_for_timeout(2000)

    def search_user(self, uname):
        
        username_field = self.page.locator("input.oxd-input.oxd-input--active").nth(1)
        username_field.wait_for(state="visible")
        username_field.fill(uname)

        
        self.page.locator("button:has-text('Search')").click()

       
        self.page.wait_for_timeout(2000)

    def click_edit_user(self):
        self.page.wait_for_selector("//div[@class='oxd-table-card']", timeout=5000)
        edit_button = self.page.locator("//div[@class='oxd-table-card']//i[contains(@class, 'bi-pencil-fill')]")
        edit_button.first.wait_for(state="visible", timeout=5000)
        edit_button.first.click()

    def edit_user_role_to_admin(self):
        
        self.page.locator("//label[text()='User Role']/following::div[@class='oxd-select-text'][0]").click()

        
        self.page.locator("//div[@role='listbox']//span[text()='Admin']").click()

        
        self.page.locator("button:has-text('Save')").click()



    def delete_user(self):
        checkbox = self.page.locator("//div[@role='row']//input[@type='checkbox']").first
        checkbox.wait_for(state="visible", timeout=5000)
        checkbox.click(force=True)

        self.delete_button.wait_for(state="visible", timeout=5000)
        self.delete_button.click()

        self.confirm_delete.wait_for(state="visible", timeout=5000)
        self.confirm_delete.click()
