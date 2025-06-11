from playwright.sync_api import Page, expect
from .base_page import BasePage
import time

class AdminPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.admin_menu = "span.oxd-text:has-text('Admin')"
        self.add_button = "button.oxd-button:has-text('Add')"
        self.user_role_dropdown = "(//div[@class='oxd-select-text--after'])[1]"
        self.employee_name_input = "input[placeholder='Type for hints...']"
        self.status_dropdown = "(//div[@class='oxd-select-text--after'])[2]"
        self.username_input = "(//input[@class='oxd-input oxd-input--active'])[2]"
        self.password_input = "(//input[@type='password'])[1]"
        self.confirm_password_input = "(//input[@type='password'])[2]"
        self.save_button = "button[type='submit']:has-text('Save')"
        self.search_username_input = ":nth-match(input.oxd-input, 2)"
        self.search_button = "button:has-text('Search')"
        self.edit_button = "i.bi-pencil-fill"
        self.delete_button = "i.bi-trash"
        self.confirm_delete_button = "button:has-text('Yes, Delete')"
        self.user_table_row = ".oxd-table-row"
        self.toast_message = ".oxd-toast-container"
        self.no_records_found = "span:has-text('No Records Found')"
        self.user_role_options = "div[role='option']"
        self.employee_autocomplete_option = "div.oxd-autocomplete-option"

    def navigate_to_admin_module(self):
        """Navigate to Admin module"""
        self.click(self.admin_menu)
        self.wait_for_element(self.add_button)

    def add_user(self, user_data):
        """Add a new user with provided data"""
        self.click(self.add_button)
        
       
        self.click(self.user_role_dropdown)
        self.click(f"div[role='option']:has-text('{user_data['role']}')")
        
        
        self.fill(self.employee_name_input, user_data['employee_name'])
        self.page.wait_for_timeout(5000)
        self.wait_for_element(f"div[role='option']")  
        self.click(f"div[role='option']:nth-child(1)")
        
        
        self.click(self.status_dropdown)
        self.click(f"div[role='option']:has-text('{user_data['status']}')")
        
       
        self.fill(self.username_input, user_data['username'])
        self.fill(self.password_input, user_data['password'])
        self.fill(self.confirm_password_input, user_data['password'])
        
        
        self.click(self.save_button)
        self.verify_success_message("Successfully Saved")

    def search_user(self, username):
        """Search for a user by username"""
        self.fill(self.search_username_input, username)
        self.click(self.search_button)
        time.sleep(1)  

    def edit_user(self, old_username, new_user_data):
        """Edit an existing user's details"""
        self.search_user(old_username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{old_username}')")
        row.locator(self.edit_button).click()
        self.wait_for_element(self.save_button)

        if 'username' in new_user_data:
            self.page.locator(self.username_input).fill('')
            self.fill(self.username_input, new_user_data['username'])
        
        if 'role' in new_user_data:
            self.click(self.user_role_dropdown)
            self.click(f"div[role='option']:has-text('{new_user_data['role']}')")
        
        if 'status' in new_user_data:
            self.click(self.status_dropdown)
            self.click(f"div[role='option']:has-text('{new_user_data['status']}')")
        
        self.click(self.save_button)
        self.verify_success_message("Successfully Updated")

    def edit_user_role(self, username, new_role):
        """Edit only the user role for an existing user"""
        self.search_user(username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{username}')")
        row.locator(self.edit_button).click()
        self.wait_for_element(self.user_role_dropdown)
        self.click(self.user_role_dropdown)
        self.click(f"div[role='option']:has-text('{new_role}')")
        self.click(self.save_button)
        self.wait_for_element(self.toast_message)
        assert "Success" in self.page.inner_text(self.toast_message)

    def get_user_role(self, username):
        """Get the current role of a specific user"""
        self.search_user(username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{username}')")
        return row.locator("div.oxd-table-cell:nth-child(3)").inner_text()    

    def delete_user(self, username):
        """Delete a user by username"""
        self.search_user(username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{username}')")
        row.locator(self.delete_button).click()
        self.click(self.confirm_delete_button)
        self.verify_success_message("Successfully Deleted")

    def is_user_found(self, username):
        """Check if user exists in search results"""
        self.search_user(username)
        return not self.page.is_visible(self.no_records_found)

    def verify_success_message(self, expected_message):
        """Verify toast message contains expected text"""
        self.wait_for_element(self.toast_message)
        toast = self.page.locator(self.toast_message)
        expect(toast).to_contain_text(expected_message)
        time.sleep(1) 

    def get_user_details(self, username):
        """Get user details from table"""
        self.search_user(username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{username}')")
        return {
            "username": username,
            "role": row.locator("div.oxd-table-cell:nth-child(3)").inner_text(),
            "status": row.locator("div.oxd-table-cell:nth-child(5)").inner_text()
        }
