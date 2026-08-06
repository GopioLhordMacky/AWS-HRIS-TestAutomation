import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from helpers import setup_browser, login_helper
from locators import Options, Table


@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_015(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # Grab the status dropdown element
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)

    # --- Keyboard Navigation: Select 'Inactive' ---
    dropdown_el.click()
    dropdown_el.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    # Verify dropdown selection changed to Inactive
    wait.until(lambda d: select.first_selected_option.text.strip() == "Inactive")
    assert select.first_selected_option.text.strip() == "Inactive"

    # Verify table updates and ALL rows reflect INACTIVE status (checkbox is UNCHECKED)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    
    # Locate all active/inactive toggle inputs in the current table rows
    inactive_toggles = driver.find_elements(By.XPATH, f"{Table.BODY}//input[@type='checkbox']")
    
    # If rows exist, verify NONE of the checkboxes are checked
    if inactive_toggles:
        for toggle in inactive_toggles:
            assert not toggle.is_selected(), "Expected all row toggles to be unchecked for INACTIVE status."

    # --- Keyboard Navigation: Select 'Active' ---
    dropdown_el.send_keys(Keys.ARROW_UP, Keys.ENTER)

    # Verify dropdown selection changed back to Active
    wait.until(lambda d: select.first_selected_option.text.strip() == "Active")
    assert select.first_selected_option.text.strip() == "Active"

    # Verify table updates and ALL rows reflect ACTIVE status (checkbox is CHECKED)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    
    active_toggles = driver.find_elements(By.XPATH, f"{Table.BODY}//input[@type='checkbox']")
    
    # Verify ALL of the checkboxes are checked
    assert len(active_toggles) > 0, "Expected active records to be listed in table."
    for toggle in active_toggles:
        assert toggle.is_selected(), "Expected all row toggles to be checked for ACTIVE status."