from selenium.webdriver.common.by import By

#Non-collapsible sidebar locators
class SidebarLocators:
    SIDEBAR = (By.XPATH, "//div[@class='sidePanelInnerContainer']")
    #SIDEBAR_HOME = (By.XPATH, "//h1[normalize-space()='Home']")
    SIDEBAR_EMPLOYEE = (By.XPATH, "//h1[normalize-space()='Employee']")
    SIDEBAR_EMPLOYEE_SETTINGS = (By.XPATH, "//h1[normalize-space()='Employee Settings']")
    SIDEBAR_SYSTEM_SETTINGS = (By.XPATH, "//h1[normalize-space()='System Settings']")
    MENU_ITEMS = (By.CSS_SELECTOR, ".menu li")

    # Pages Sidebar Items
    CLIENT_MENU = (
        By.XPATH,
        "//span[contains(@class,'navLinkText')][normalize-space()='Client']"
    )

    FISCAL_YEAR_MENU = (
        By.XPATH,
        "//span[contains(@class,'navLinkText')][normalize-space()='Fiscal Year']"
    )

    LOCATION_MENU = (
        By.XPATH,
        "//span[contains(@class,'navLinkText')][normalize-space()='Location']"
    )


# For collapsible sidebar - not currently implemented, but keeping here for future reference
# class CollapsibleSidebarLocators:
#     SIDEBAR = (By.ID, "sidebar")
#     MENU_ITEMS = (By.CSS_SELECTOR, ".menu li")
#     COLLAPSE_BUTTON = (By.CLASS_NAME, "toggle") 