from .base_page import BasePage

class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.admin_menu = "span:has-text('Admin')"
        self.add_button = "button:has-text('Add')"
        self.user_role_dropdown = ".oxd-select-text--after"
        self.employee_name_input = "input[placeholder='Type for hints...']"
        self.status_dropdown = "(//div[@class='oxd-select-text--after'])[2]"
        self.username_input = "(//input[@class='oxd-input oxd-input--active'])[2]"
        self.password_input = "(//input[@type='password'])[1]"
        self.confirm_password_input = "(//input[@type='password'])[2]"
        self.save_button = "button:has-text('Save')"
        self.search_username_input = ":nth-match(input.oxd-input, 2)"
        self.search_button = "button:has-text('Search')"
        self.edit_button = "i.bi-pencil-fill"  
        self.delete_button = "i.bi-trash"  
        self.confirm_delete_button = "button:has-text('Yes, Delete')"
        self.user_table_row = ".oxd-table-row"
        self.toast_message = ".oxd-toast-container"
        self.user_role_in_table = "(//div[contains(@class, 'oxd-table-cell')][3]"  
        self.status_in_table = "(//div[contains(@class, 'oxd-table-cell')][5]"  
    
    def navigate_to_admin_module(self):
        self.click(self.admin_menu)
    
    def add_user(self, user_data):
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
        self.wait_for_element(self.toast_message)
    
    def search_user(self, username):
        self.fill(self.search_username_input, username)
        self.click(self.search_button)
        self.wait_for_element(self.user_table_row)
    
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
        self.search_user(username)
        row = self.page.locator(f"div.oxd-table-row:has-text('{username}')")
        row.locator(self.delete_button).click()
        self.click(self.confirm_delete_button)
        self.wait_for_element(self.toast_message)
    
    def is_user_found(self, username):
        self.search_user(username)
        return self.page.locator(self.user_table_row).count() > 0
    
    def get_user_details(self, username):
        """Get user role and status from table"""
        self.search_user(username)
        role = self.page.locator(self.user_role_in_table).first.inner_text()
        status = self.page.locator(self.status_in_table).first.inner_text()
        return {"role": role, "status": status}