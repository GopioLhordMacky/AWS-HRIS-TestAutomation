import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators.client_page_locators import *
from imports.main_imports.main_imports import *

def is_component_visible(driver, locator, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False

def is_component_clickable(driver, locator, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        return True
    except TimeoutException:
        return False

def verify_dropdown_options(driver, dropdown_locator, expected_options, options_locator=None, timeout=5):
    """
    Opens a dropdown menu (including native <select>), verifies that all expected options 
    are present, and closes/resets focus. Supports standard HTML <select> and custom React/MUI components.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        
        # Step 1: Ensure element is visible/clickable and click to open
        dropdown_elem = wait.until(EC.element_to_be_clickable(dropdown_locator))
        dropdown_elem.click()
        time.sleep(0.5)  # Brief delay to visually see the click interaction
        
        # Step 2: Handle Native HTML <select> Tag
        if dropdown_elem.tag_name.lower() == "select":
            select = Select(dropdown_elem)
            actual_options = [opt.text.strip() for opt in select.options if opt.text.strip()]
            
        # Step 3: Handle Custom UI Dropdowns (React / MUI / Custom)
        else:
            if not options_locator:
                options_locator = (
                    By.XPATH,
                    ".//option | //div[contains(@id, '-option-') or contains(@class, '-option') or @role='option'] | //li[@role='option']"
                )

            # Look within element first, then fallback globally
            option_elements = dropdown_elem.find_elements(*options_locator)
            if not option_elements:
                wait.until(EC.presence_of_element_located(options_locator))
                option_elements = driver.find_elements(*options_locator)

            actual_options = [elem.text.strip() for elem in option_elements if elem.text.strip()]

            # Close custom dropdown by clicking it again
            try:
                dropdown_elem.click()
            except Exception:
                pass

        # Step 4: Perform case-insensitive comparison
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
    
def verify_input_is_empty(driver, locator, timeout=5):
    """
    Verifies whether an input or textarea field is completely empty.

    """
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))

        # Standard inputs use the 'value' attribute; textareas might fall back to .text
        value = element.get_attribute("value") or element.text

        # Strip whitespace to handle cases where inputs only contain spaces
        is_empty = value.strip() == ""

        if not is_empty:
            print(f"[Input Check Failed] Field expected to be empty, but contained: '{value}'")

        return is_empty

    except Exception as e:
        print(f"[Input Check Exception] {e}")
        return False

def verify_input_matches(driver, locator, expected_text, timeout=5):
    """
    Verifies that an input field, textarea, or react-select dropdown matches an expected text.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))

        # Check for react-select value containers (common class structures in react-select)
        react_single_value = element.find_elements(By.XPATH, ".//ancestor::div[contains(@class, 'select__control')]//div[contains(@class, 'select__single-value')]")
        
        if react_single_value:
            actual_text = react_single_value[0].text.strip()
        else:
            # Fallback for standard input attributes or textareas
            actual_text = (element.get_attribute("value") or element.text or "").strip()

        matches = actual_text == expected_text.strip()

        if not matches:
            print(f"[Input Text Match Failed] Expected: '{expected_text}', Actual: '{actual_text}'")

        return matches

    except Exception as e:
        print(f"[Input Text Match Exception] {e}")
        return False
