from config.config import BASE_URL
from config.route import *
from pages.sidebar_page import Sidebar
from pages.employee_list_page import EmployeeListPage
from pages.client_page import ClientPage

def go_to_client_page(driver, via="url"):
    if via == "url":
        driver.get(f"{BASE_URL}{CLIENT}")
        # print(f"[Navigation] Navigating to Client Page via URL: {BASE_URL}{CLIENT}")
    elif via == "sidebar":
        sidebar = Sidebar(driver)
        sidebar.click_client_menu()
    else:
        raise ValueError(f"Unknown navigation method: {via}")
    return ClientPage(driver)

