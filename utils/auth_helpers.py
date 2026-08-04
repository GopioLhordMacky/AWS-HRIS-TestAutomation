from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage

def login_and_initial_setup(driver, username, password):
    """
    Universal entry point: 
    1. Performs the login action.
    2. Waits for the landing page (Birthday Celebrants) to be fully ready.
    This prevents 'Element Not Found' errors on subsequent navigation steps.
    """
    login_page = LoginPage(driver)
    print(f"[Auth] Logging in")
    login_page.login(username, password)
    
    employee_list_page = EmployeeListPage(driver)
    print("[Auth] Waiting for Employee List Page to load...")
    employee_list_page.wait_until_loaded()
    print("[Auth] Login successful: Session is now ready for navigation.")
    return employee_list_page