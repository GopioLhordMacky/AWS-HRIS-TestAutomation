from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.employee_list_locators import EmployeeListLocators as Locators

class EmployeeListPage(BasePage):

    def wait_until_loaded(self):
        """
        Wait until dashboard critical elements are visible.
        Raises TimeoutException if not loaded.
        """
        self.wait.until(EC.visibility_of_element_located(Locators.PAGE_TITLE))
        # self.wait.until(EC.visibility_of_element_located(Locators.EMPLOYEE_TABLE))
        self.wait.until(EC.visibility_of_element_located(Locators.ADD_EMPLOYEE_BTN))

    def is_dashboard_loaded(self):
        """
        Check if the dashboard has loaded successfully.
        Returns True if all critical elements are visible, False otherwise.
        """
        try:
            return all([
                self.is_visible(Locators.PAGE_TITLE),
                self.is_visible(Locators.EMPLOYEE_TABLE),
                self.is_visible(Locators.ADD_EMPLOYEE_BTN)
            ])
        except TimeoutException:
            return False
