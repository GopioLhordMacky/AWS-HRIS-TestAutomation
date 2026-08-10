import random
import string
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import IMPLICIT_WAIT


class BasePage:
    """
    BasePage is the parent class for all Page Objects.
    Contains robust, standardized Selenium wrappers with explicit waits,
    DOM state checks, element interaction, and keyboard navigation utilities.
    """
    def __init__(self, driver):
        """
        Initialize with the Selenium WebDriver instance and set an explicit wait.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.timeout = 10 
        self.wait = WebDriverWait(driver, IMPLICIT_WAIT)

    # =========================================================================
    # 1. CORE ELEMENT LOCATORS & SEARCH (Cleaned & Standardized)
    # =========================================================================
    def find_element(self, locator):
        """
        Finds a single element directly without locator type restrictions.
        Unpacks tuple directly (*locator) to support all Selenium By strategies.
        """
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            print(f"Error finding element with locator {locator}: {e}")
            return None
    
    def find_elements(self, by, value):
        """
        Non-tuple wrapper that finds a single element using separate 'by' and 'value' arguments.
        Leaves existing find_element(self, locator) completely intact.
        
        Example: page.find_elements(By.XPATH, "//tbody/tr[1]/td[2]")
        """
        try:
            return self.driver.find_element(by, value)
        except Exception as e:
            print(f"Error finding element with {by}='{value}': {e}")
            return None

    def find_elements_len(self, by, value):
        """
        Non-tuple wrapper that finds multiple elements using separate 'by' and 'value' arguments.
        Returns a list of WebElements so len() works seamlessly.
        
        Example: row_count = len(page.find_elements(By.XPATH, "//tbody/tr/td[1]"))
        """
        try:
            return self.driver.find_elements(by, value)
        except Exception as e:
            print(f"Error finding elements with {by}='{value}': {e}")
            return []

    def find(self, locator):
        """Alias for find_element to maintain backward compatibility."""
        return self.find_element(locator)

    def find_all(self, locator):
        """Returns a list of WebElements matching the provided locator."""
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            print(f"Error finding elements with locator {locator}: {e}")
            return []

    # =========================================================================
    # 2. STANDARDIZED ACTION WRAPPERS (With Explicit Waits)
    # =========================================================================
    def click(self, locator):
        """
        Waits until the element located by 'locator' is clickable, then clicks it.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return element
        except Exception as e:
            print(f"Error clicking element with locator {locator}: {e}")
            raise

    def wait_for_and_click(self, locator):
        """Alias for click to support existing child page implementations."""
        return self.click(locator)

    def type(self, locator, text, clear_first=True):
        """
        Waits until the element located by 'locator' is visible, clears existing text
        (if clear_first=True), and inputs the provided text.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear_first:
                element.clear()
            element.send_keys(text)
            return element.get_attribute("value")
        except Exception as e:
            print(f"Error typing into element with locator {locator}: {e}")
            raise

    def wait_and_type(self, locator, text="", clear_first=True):
        """Alias for type to support existing child page implementations."""
        return self.type(locator, text, clear_first=clear_first)

    def wait_for_and_click (self, locator):
        return self.click(locator)

    def verify_input_is_empty(self, locator) -> bool:
        """
        Checks if an input or textarea element's value is empty or contains only whitespace.

        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        # Retrieves value from 'value' attribute or visible text (for custom select/dropdown wrappers)
        value = element.get_attribute("value") or element.text or ""
        return value.strip() == ""

    def input_text(self, locator, text):
        """Consolidated alias for type() to prevent breaking legacy calls."""
        return self.type(locator, text, clear_first=True)

    def clear_input_field(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)

    def get_text(self, locator) -> str:
        """
        Waits until the element is visible and returns its text content.
        Falls back to 'textContent' DOM attribute if standard text is empty.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text.strip()
            if not text:
                text = element.get_attribute("textContent").strip()
            return text
        except TimeoutException:
            print(f"Element not found or not visible: {locator}")
            return ""
        except Exception as e:
            print(f"Unexpected error retrieving text for locator {locator}: {e}")
            return ""

    def get_text_from_element(self, element, locator) -> str:
        """
        Gets the text of a child element scoped inside a parent WebElement.
        """
        try:
            child = element.find_element(*locator)
            return child.text.strip()
        except Exception as e:
            print(f"Error getting text from child element with locator {locator}: {e}")
            return ""

    # =========================================================================
    # 3. DOM & VISIBILITY UTILITIES
    # =========================================================================
    def ensure_element_visible(self, locator):
        """Waits until an element is visible in the DOM and returns it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator) -> bool:
        """Checks if an element is visible on the page."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_present(self, locator) -> bool:
        """Checks if an element exists in the DOM regardless of visibility."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def has_elements(self, locator) -> bool:
        """Checks if at least one matching element exists in the DOM."""
        return len(self.find_all(locator)) > 0

    def wait_until_not_visible(self, locator) -> bool:
        """Waits until an element is no longer visible in the DOM."""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_elements(self, locator):
        """Waits until all matching elements are present in the DOM."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Timed out waiting for elements with locator: {locator}")
            raise

    def wait_until(self, condition_func):
        """Generic wait wrapper executing a custom lambda or expected condition."""
        try:
            return self.wait.until(condition_func)
        except TimeoutException:
            raise TimeoutException(f"Condition not met within {self.timeout} seconds.")

    def refresh_page(self):
        """
        Refreshes the page natively and waits until the browser DOM reports complete.
        Replaces hardcoded sleep with DOM readiness check.
        """
        print("Refreshing the page...")
        self.driver.refresh()
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # =========================================================================
    # 4. FORM & COMPONENT CONTROLS
    # =========================================================================
    def is_radio_selected(self, locator) -> bool:
        """Checks if a radio button or checkbox is selected."""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_selected()
        except TimeoutException:
            return False

    def is_toggle_on(self, locator) -> bool:
        """Checks if a toggle/checkbox element has the 'checked' attribute."""
        try:
            toggle_button = self.find_element(locator)
            if toggle_button:
                return toggle_button.get_attribute("checked") is not None
            return False
        except Exception as e:
            print(f"Error checking if toggle is on with locator {locator}: {e}")
            return False

    def get_dropdown_options(self, select_locator: tuple) -> list:
        """Retrieves options from a native HTML <select> dropdown."""
        try:
            select_element = self.wait.until(
                EC.presence_of_element_located(select_locator),
                message=f"Dropdown select element {select_locator} not found."
            )
            select_object = Select(select_element)
            return [option.text.strip() for option in select_object.options]
        except Exception as e:
            print(f"Error getting dropdown options for {select_locator}: {e}")
            return []

    def get_selected_option(self, select_locator: tuple) -> str:
        """Returns the active option in a native HTML <select> dropdown."""
        try:
            select_element = self.wait.until(
                EC.presence_of_element_located(select_locator),
                message=f"Dropdown select element {select_locator} not found."
            )
            select_object = Select(select_element)
            return select_object.first_selected_option.text.strip()
        except Exception as e:
            print(f"Error getting active selected option for {select_locator}: {e}")
            return ""

    def wait_for_toast_message(self, locator):
        """Waits for a toast notification element to become visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("Toast message did not appear within the specified time.")
            return None

    def is_sidebar_link_visible(self, nav_locator) -> bool:
        """Checks if a sidebar navigation link is displayed."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(nav_locator))
            return element.is_displayed()
        except TimeoutException:
            print(f"Sidebar Timeout: Element matching locator '{nav_locator}' was not found or is hidden.")
            return False

    def is_tab_active(self, tab_locator) -> bool:
        """Checks if a UI tab element has active selection attributes."""
        try:
            tab_element = self.wait.until(EC.presence_of_element_located(tab_locator))
            aria_selected = tab_element.get_attribute("aria-selected")
            if aria_selected == "true":
                return True
            class_attribute = tab_element.get_attribute("class") or ""
            return "selected" in class_attribute or "active" in class_attribute
        except TimeoutException:
            print(f"Element matching locator '{tab_locator}' was not found.")
            return False

    def get_first_row_values(self, container_locator):
        """Extracts text contents from the cells of the first table row in a container."""
        try:
            container = self.find_element(container_locator)
            if not container:
                return []

            row_xpath = ".//table//tbody/tr"

            def rows_loaded(driver):
                rows = container.find_elements(By.XPATH, row_xpath)
                if not rows or rows[0].text.strip() == "":
                    return False
                return rows

            rows = self.wait.until(rows_loaded)
            first_row = rows[0]
            cells = first_row.find_elements(By.XPATH, ".//td")
            return [cell.text.strip() for cell in cells]
        except Exception as e:
            print(f"Error extracting first row values for {container_locator}: {e}")
            return []

    def get_values_from_locators(self, locators: dict, attribute="value") -> dict:
        """Reads attributes or text values from a mapping dictionary of field locators."""
        values = {}
        for field_name, locator in locators.items():
            element = self.find_element(locator)
            if element is None:
                values[field_name] = ""
                continue
            try:
                val = element.get_attribute(attribute)
                values[field_name] = val if val is not None else element.text.strip()
            except Exception as e:
                print(f"Error reading field '{field_name}' with locator {locator}: {e}")
                values[field_name] = ""
        return values

    # =========================================================================
    # 5. KEYBOARD NAVIGATION & ACCESSIBILITY HELPERS
    # =========================================================================
    def get_focused_element_identifier(self) -> str:
        """Returns the best identifier (ID, name, text, type, or tag) of the focused element."""
        active_element = self.driver.switch_to.active_element
        element_id = active_element.get_attribute("id")
        if element_id:
            return element_id
        element_name = active_element.get_attribute("name")
        if element_name:
            return element_name
        element_text = active_element.text.strip()
        if element_text:
            return element_text
        element_type = active_element.get_attribute("type")
        if element_type:
            return f"type-{element_type}"
        return active_element.tag_name

    def verify_complete_tab_order(self, start_locator: tuple, expected_identifiers: list) -> list:
        """Navigates sequentially using TAB keypresses and records focus path."""
        actual_focus_path = []
        start_element = self.wait.until(EC.element_to_be_clickable(start_locator))
        start_element.click()
        time.sleep(0.3)

        for _ in range(len(expected_identifiers)):
            self.driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(0.2)
            actual_focus_path.append(self.get_focused_element_identifier())

        return actual_focus_path

    def send_keys_to_element(self, locator, keys):
        """Sends specific keyboard keys (e.g., Keys.TAB, Keys.ENTER) to an element."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(keys)
        except Exception as e:
            print(f"Error sending keys to element with locator {locator}: {e}")
            raise

    def press_tab_key(self, locator: tuple = None):
        """Simulates a TAB key stroke to a target locator or global focus path."""
        if locator:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.send_keys(Keys.TAB)
        else:
            ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def press_enter_key(self, locator: tuple = None):
        """Simulates an ENTER key stroke to a target locator or global focus path."""
        if locator:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.send_keys(Keys.ENTER)
        else:
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def press_space_key(self, locator: tuple = None):
        """Simulates a SPACE key stroke to a target locator or global focus path."""
        if locator:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.send_keys(Keys.SPACE)
        else:
            ActionChains(self.driver).send_keys(Keys.SPACE).perform()

    def press_escape_key(self):
        """Fires a global ESCAPE key stroke on the body element."""
        try:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        except Exception as e:
            print(f"Failed to execute keyboard Escape action: {e}")

    # =========================================================================
    # 6. DATA GENERATION UTILITIES
    # =========================================================================
    def valid_name_and_alias_creation(self) -> str:
        """Generates a valid random string (length 2-30) containing special characters."""
        special_chars = "&.,'-"
        total_length = random.randint(2, 30)
        allowed_chars = string.ascii_letters + string.digits + special_chars
        chars = [random.choice(special_chars)]
        if total_length > 1:
            chars.extend(random.choices(allowed_chars, k=total_length - 1))
        random.shuffle(chars)
        return "".join(chars)

    def invalid_name_and_alias_creation(self, scenario: str):
        """Generates invalid boundary strings based on the target test scenario."""
        invalid_special_chars = list("!@#$%^*()+=[]{}|\\<>?/`~\";:")
        if scenario == "invalid_special_chars":
            return f"{invalid_special_chars[0]}test"
        if scenario == "leading_space":
            return "  invalid"
        if scenario == "trailing_space":
            return "invalid  "
        if scenario == "double_space":
            return "inva  lid"
        if scenario == "min_length":
            return "a"
        if scenario == "max_length":
            return "a" * 31
        if scenario == "invalid_char_loop":
            return invalid_special_chars
        return "invalid-default"

    def valid_data_creation(self) -> str:
        """Generates a valid random string up to 255 characters with a special character."""
        special_chars = "&.,'-"
        total_length = random.randint(2, 255)
        allowed_chars = string.ascii_letters + string.digits + special_chars
        chars = [random.choice(special_chars)]
        if total_length > 1:
            chars.extend(random.choices(allowed_chars, k=total_length - 1))
        random.shuffle(chars)
        return "".join(chars)

    def get_column_values(self, column_index: int) -> list:
        """
        Extracts all text values from a specific column in the data table.
        :param column_index: 1-based index of the column (e.g., 2 for Department Name)
        """
        # Locates all row cells under that specific column index
        cell_locator = (By.XPATH, f"//table/tbody/tr/td[{column_index}]")
        
        # Wait for the elements to be present
        cells = self.wait.until(EC.presence_of_all_elements_located(cell_locator))
        
        # Extract the clean, trimmed text from each cell
        return [cell.text.strip() for cell in cells if cell.text.strip()]

    def is_list_sorted(self, data_list: list, reverse=False) -> bool:
        """Returns True if the list matches its sorted version."""
        return data_list == sorted(data_list, reverse=reverse)
    
    # ----------------------------------------------------------------------------------------

    # ------------------------------ Status Filter Switching Methods ------------------------------
    def change_status_filter(self, dropdown_locator: tuple, status_text: str):
        """
        Universally selects a status option from standard HTML <select> dropdowns.
        
        :param dropdown_locator: Tuple locator for the <select> element
        :param status_text: The visible text of the option to select (e.g., "ACTIVE", "INACTIVE")
        """
        # 1. Wait for the select element to be present
        dropdown_element = self.wait.until(EC.presence_of_element_located(dropdown_locator))
        
        # 2. Use the Select support class
        select = Select(dropdown_element)
        
        # 3. Select by visible text (standardizes against "ACTIVE" vs "Active")
        # Note: .select_by_visible_text() is case-sensitive. Ensure the input matches the option text exactly.
        select.select_by_visible_text(status_text.upper())