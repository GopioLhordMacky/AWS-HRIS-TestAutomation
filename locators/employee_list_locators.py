from selenium.webdriver.common.by import By

class EmployeeListLocators:
    """Locators for Employee List Dashboard page"""
    # Header elements
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Employee List']")

    # Table elements
    EMPLOYEE_TABLE = (By.XPATH, "//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiTableContainer-root reusable-table-scroll css-frjz7u']")

    # Action buttons
    ADD_EMPLOYEE_BTN = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")