import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from components.tables import Table
from pages.base_page import BasePage

class Element(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_component_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_component_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except Exception:
            return False

    def verify_dropdown_options(self, dropdown_locator, expected_options, options_locator=None):
        try:
            dropdown_elem = self.wait.until(EC.element_to_be_clickable(dropdown_locator))
            dropdown_elem.click()
            time.sleep(0.5)
            
            if dropdown_elem.tag_name.lower() == "select":
                select = Select(dropdown_elem)
                actual_options = [opt.text.strip() for opt in select.options if opt.text.strip()]
            else:
                if not options_locator:
                    options_locator = (
                        By.XPATH,
                        ".//option | //div[contains(@id, '-option-') or contains(@class, '-option') or @role='option'] | //li[@role='option']"
                    )

                option_elements = dropdown_elem.find_elements(*options_locator)
                if not option_elements:
                    self.wait.until(EC.presence_of_element_located(options_locator))
                    option_elements = self.driver.find_elements(*options_locator)

                actual_options = [elem.text.strip() for elem in option_elements if elem.text.strip()]

                try:
                    dropdown_elem.click()
                except Exception:
                    pass

            actual_lower = [opt.lower() for opt in actual_options]
            missing_options = [opt for opt in expected_options if opt.lower() not in actual_lower]

            if missing_options:
                print(f"[verify_dropdown_options] Mismatch!")
                print(f" -> Expected: {expected_options}")
                print(f" -> Found in DOM: {actual_options}")
                print(f" -> Missing: {missing_options}")
                return False

            return True

        except Exception as e:
            print(f"[verify_dropdown_options] Exception encountered: {e}")
            return False

    def verify_input_is_empty(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            value = element.get_attribute("value") or element.text
            is_empty = value.strip() == ""

            if not is_empty:
                print(f"[Input Check Failed] Field expected to be empty, but contained: '{value}'")

            return is_empty

        except Exception as e:
            print(f"[Input Check Exception] {e}")
            return False

    def verify_input_matches(self, locator, expected_text):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            react_single_value = element.find_elements(By.XPATH, ".//ancestor::div[contains(@class, 'select__control')]//div[contains(@class, 'select__single-value')]")
            
            if react_single_value:
                actual_text = react_single_value[0].text.strip()
            else:
                actual_text = (element.get_attribute("value") or element.text or "").strip()

            matches = actual_text == expected_text.strip()

            if not matches:
                print(f"[Input Text Match Failed] Expected: '{expected_text}', Actual: '{actual_text}'")

            return matches

        except Exception as e:
            print(f"[Input Text Match Exception] {e}")
            return False

    def select_custom_dropdown(self, dropdown_label, option_text):
        self.wait_for_and_click(DropdownLocators.DROPDOWN_CONTAINER_BY_LABEL(dropdown_label))
        self.wait_for_and_click(DropdownLocators.DROPDOWN_OPTION(option_text))

    def select_react_dropdown(self, locator, option_text):
        """
        Handles React-Select and modern custom dropdowns by typing and selecting an option.
        
        :param locator: Tuple (By, value) representing the dropdown input element
        :param option_text: String text of the option to search and select
        """
        try:
            # 1. Wait until the input element is ready to accept interaction
            dropdown_input = self.wait.until(EC.element_to_be_clickable(locator))
            
            # 2. Click to open/focus, clear existing text, and type search string
            dropdown_input.click()
            dropdown_input.send_keys(Keys.CONTROL + "a")
            dropdown_input.send_keys(Keys.BACKSPACE)
            dropdown_input.send_keys(option_text)
            
            # 3. Wait for option container or menu item to appear, then select
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{option_text}')]"))
            )
            dropdown_input.send_keys(Keys.ENTER)
            
            return self
            
        except TimeoutException:
            print(f"Failed to locate or select option '{option_text}' in React dropdown {locator}")
            raise

    def toggle_active_status(self, row_index, column_name="Active"):
        col_idx = self.get_column_index(column_name)
        self.wait_for_and_click(ToggleSwitchLocators.TOGGLE_BY_ROW_AND_COL(row_index, col_idx))

    def verify_active_toggle_state(self, row_index, column_name="Active"):
        col_idx = self.get_column_index(column_name)
        element = self.driver.find_element(*ToggleSwitchLocators.TOGGLE_BY_ROW_AND_COL(row_index, col_idx))
        return element.is_selected()