from locators.shared.shared_locators import LoginLocators
from locators.shared.shared_locators import TabNavigationLocators
from helpers.main_helpers.setup_browser import wait_and_type, wait_for_and_click, ensure_element_visible

def login(driver, username, password, url="https://test.hris2.awsys-i.com/employee-list"):
    if url:
        driver.get(url)
    wait_and_type(driver, *LoginLocators.USERNAME_INPUT, text=username)
    wait_and_type(driver, *LoginLocators.PASSWORD_INPUT, text=password)
    wait_for_and_click(driver, *LoginLocators.LOGIN_BTN)
    return ensure_element_visible(driver, *LoginLocators.USER_AVATAR)

def navigate_to_page(driver, page_name):
    wait_for_and_click(driver, *LoginLocators.SIDEBAR_MENU_ITEM(page_name))

def switch_tab(driver, tab_name):
    wait_for_and_click(driver, *TabNavigationLocators.SUB_TAB_BY_NAME(tab_name))