from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.sidebar_locators import SidebarLocators as Locators
from pages.base_page import BasePage

class Sidebar(BasePage):

    def is_visible(self):
        """Checks that all major sidebar sections are loaded and visible."""
        try:
            # Define the locators we want to verify
            sections = [
                Locators.SIDEBAR_EMPLOYEE,
                Locators.SIDEBAR_EMPLOYEE_SETTINGS,
                Locators.SIDEBAR_SYSTEM_SETTINGS
            ]
            
            # Wait for all of them to be visible
            elements = [self.wait.until(EC.visibility_of_element_located(loc)) for loc in sections]
            
            # Return True only if every element in the list is currently displayed
            return all(el.is_displayed() for el in elements)
            
        except Exception as e:
            print(f"[Sidebar] One or more sections failed to load: {e}")
            return False

    def click_client_menu(self):
        self.click(Locators.CLIENT_MENU)

    def is_item_visible_under_section(self, section_name, item_name):

        xpath = (
            f"//*[normalize-space()='{section_name}']"
            f"/following::*[normalize-space()='{item_name}'][1]"
        )
        print(f"Constructed XPath for sidebar item: {xpath}")

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False


    # ------------------------------------------------------------
    # for future if sidebar becomes collapsible
    # class CollapsibleSidebar:
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(driver, 10)

    # def is_visible(self):
    #     """
    #     Check if the sidebar is visible
    #     """
    #     sidebar = self.wait.until(EC.presence_of_element_located(CollapsibleSidebarLocators.SIDEBAR))
    #     return sidebar.is_displayed()

    # def navigate_to(self, nav_locator, expected_page_locator=None):
    #     """
    #     Click a sidebar menu item.
    #     Optionally waits for an expected page element to appear.
    #     """
    #     try:
    #         menu_link = self.wait.until(EC.element_to_be_clickable(nav_locator))
    #         menu_link.click()

    #         if expected_page_locator:
    #             self.wait.until(EC.presence_of_element_located(expected_page_locator))
    #         return True
    #     except TimeoutException:
    #         print(f"Navigation failed for locator: {nav_locator}")
    #         return False

    # def collapse(self):
    #     """
    #     Collapse the sidebar
    #     """
    #     try:
    #         collapse_btn = self.driver.find_element(*CollapsibleSidebarLocators.COLLAPSE_BUTTON)
    #         collapse_btn.click()
    #         return True
    #     except Exception:
    #         print("Collapse button not found")
    #         return False

    # def expand(self):
    #     """
    #     Expand the sidebar
    #     """
    #     try:
    #         collapse_btn = self.driver.find_element(*CollapsibleSidebarLocators.COLLAPSE_BUTTON)
    #         collapse_btn.click()
    #         return True
    #     except Exception:
    #         print("Expand button not found")
    #         return False