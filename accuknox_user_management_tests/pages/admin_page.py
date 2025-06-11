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
        
        self.save_button.click()

        
        self.page.wait_for_timeout(2000)

    def search_user(self, uname):
        self.search_input.fill(uname)
        self.search_button.click()

    def edit_user(self):
    
        user_locator = self.page.locator("//div[@role='rowgroup']//div[contains(text(),'testuser1')]")

        
        user_locator.wait_for(timeout=5000)

        self.edit_button.wait_for(state="visible", timeout=5000)
        self.edit_button.click()

        self.status.click()
        self.page.get_by_text("Disabled", exact=True).click()

        self.save_button.click()





    def delete_user(self):
        checkbox = self.page.locator("//div[@role='row']//input[@type='checkbox']").first
        checkbox.wait_for(state="visible", timeout=5000)
        checkbox.click(force=True)

        self.delete_button.wait_for(state="visible", timeout=5000)
        self.delete_button.click()

        self.confirm_delete.wait_for(state="visible", timeout=5000)
        self.confirm_delete.click()