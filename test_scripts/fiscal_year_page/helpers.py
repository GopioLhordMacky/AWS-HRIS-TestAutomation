import pytest
from plugins import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Fiscal_Year_Page.locators import Login_Locators, Sidebar_Locators, Buttons, Options, Table, Confirmation_Dialogue


@pytest.fixture
def setup_browser():
    """Fixture that initializes the driver, loads the page, and cleans up."""
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://staging.hris2.awsys-i.com/settings/fiscal-year')

    yield driver
    driver.quit()


def login_helper(driver):
    username = "macky-temp.gopio@awsys-i.com"
    password = "Awsys123@"
    wait = WebDriverWait(driver, 10)
    
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, Login_Locators.USERNAME_FIELD)))
    username_field.send_keys(username)
    
    password_field = driver.find_element(By.XPATH, Login_Locators.PASSWORD_FIELD)
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, Login_Locators.LOGIN_BUTTON)
    login_button.click()

    fiscal_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, Sidebar_Locators.FISCAL_YEAR_BUTTON))
    )        
    fiscal_button.click()


def save_btn(driver):
    wait = WebDriverWait(driver, 10)
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.SAVE_BUTTON)))
    save_button.click()


def close_btn(driver):
    """Closes modal via the 'Close' button."""
    wait = WebDriverWait(driver, 10)
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.CLOSE_BUTTON)))
    close_button.click()


def close_by_x_btn(driver):
    """Closes modal via the 'X' icon in the header."""
    wait = WebDriverWait(driver, 10)
    x_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.X_BUTTON)))
    x_btn.click()

# THIS METHOD IS NOT WORKING DUE TO DIRTY XPATH
def close_by_backdrop(driver):
    """Closes modal by clicking outside the modal dialog overlay."""
    wait = WebDriverWait(driver, 10)
    # Target the modal backdrop overlay element or clicking top-left corner outside dialog content
    backdrop = wait.until(
        EC.presence_of_element_located((
            By.XPATH, 
            "//div[contains(@class, 'MuiBackdrop-root')]"
        ))
    )
    backdrop.click()

def open_add_fiscal_year_modal(driver):
    wait = WebDriverWait(driver, 10)
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.ADD_FISCAL_YEAR_BUTTON)))
    add_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-title') or contains(text(), 'Add Fiscal Year')]")))


def fill_start_date(driver, date_str="05-2051"):
    """Fills the Start Date field using React's native value setter to guarantee state update."""
    wait = WebDriverWait(driver, 10)
    start_input = wait.until(EC.presence_of_element_located((By.XPATH, Options.START_DATE)))
    
    driver.execute_script("""
        var input = arguments[0];
        var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(input, arguments[1]);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, start_input, date_str)

    return date_str

def update_start_date(driver, date_str="05-2072"):
    """Fills the Start Date field using React's native value setter to guarantee state update."""
    wait = WebDriverWait(driver, 10)
    start_input = wait.until(EC.presence_of_element_located((By.XPATH, Options.START_DATE)))
    
    driver.execute_script("""
        var input = arguments[0];
        var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(input, arguments[1]);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, start_input, date_str)
    
    return date_str  

def filter_by_status(driver, status_text="Inactive"):
    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text(status_text)

def select_status_active(driver):
    """Selects 'Active' from the Status dropdown."""
    wait = WebDriverWait(driver, 10)
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)
    select.select_by_visible_text("Active")

def select_status_inactive(driver):
    """Selects 'Inactive' from the Status dropdown."""
    wait = WebDriverWait(driver, 10)
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)
    select.select_by_visible_text("Inactive")

def verify_table_data_present(driver):
    """Waits for table rows to be present and returns the entire text content of tbody."""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    return driver.find_element(By.XPATH, Table.BODY).text

def verify_table_search_results(driver, search_input_xpath=Options.SEARCH_FIELD):
    """
    Dynamically waits for table updates after a search operation.
    Validates that either the empty state message appears or all displayed rows 
    contain the query typed in the search field.
    """
    wait = WebDriverWait(driver, 10)
    
    # 1. Dynamically retrieve the current search term from the input field
    search_input_el = wait.until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))
    current_search_term = search_input_el.get_attribute("value").strip()

    # 2. Wait until table body reflects results matching the search term OR 'no results found'
    wait.until(
        lambda d: current_search_term in d.find_element(By.XPATH, Table.BODY).text
        or "no results found" in d.find_element(By.XPATH, Table.BODY).text.lower()
    )

    body_text = driver.find_element(By.XPATH, Table.BODY).text

    # 3. Assert outcomes
    if "no results found" in body_text.lower():
        # Passed empty state check
        assert True
    else:
        # Validate every displayed row contains the search term
        rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
        assert len(rows) > 0, f"Expected table rows for search query '{current_search_term}'."
        for row in rows:
            assert current_search_term in row.text, (
                f"Row text '{row.text}' did not contain expected search term '{current_search_term}'."
            )

def select_status(driver, status="Active"):
    """
    Selects a status from the Status dropdown.
    Accepts 'Active', 'Inactive', or any valid option text.
    """
    wait = WebDriverWait(driver, 10)
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)
    select.select_by_visible_text(status)

def fill_search_field(driver, search_str="2030"):
    """Clears the search input and fills it with the provided query string."""
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, Options.SEARCH_FIELD)))
    
    # Select all and backspace to clear reliably in React
    search_input.send_keys(Keys.CONTROL + "a" if driver.capabilities['platformName'] != 'mac' else Keys.COMMAND + "a")
    search_input.send_keys(Keys.BACKSPACE)
    
    if search_str:
        search_input.send_keys(search_str)

def click_edit_fiscal_year (driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    assert len(rows) >= 1, "Expected at least 1 row in the table to perform update."

    target_row = rows[0]
    edit_button = target_row.find_element(By.XPATH, Buttons.EDIT_BUTTON)
    wait.until(EC.element_to_be_clickable(edit_button))
    edit_button.click()

def toggle_click (driver):
    wait = WebDriverWait(driver, 10)

    # Wait for table rows to load and get initial count
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    initial_rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    initial_count = len(initial_rows)

    # --- Step 1: Cancel Scenario ---
    target_row = initial_rows[0]
    toggle_btn = target_row.find_element(By.XPATH, Options.TOGGLE_BUTTON)
    wait.until(EC.element_to_be_clickable(toggle_btn))
    toggle_btn.click()
    confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON)))
    confirm_btn.click()
    time.sleep(2) 