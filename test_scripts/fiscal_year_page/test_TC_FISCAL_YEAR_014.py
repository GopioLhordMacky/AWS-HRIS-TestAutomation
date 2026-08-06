import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from helpers import (
    setup_browser, 
    login_helper, 
    select_status_active, 
    select_status_inactive
)
from locators import Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_014(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # Grab dropdown instance for assertions
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)

    # --- Step 5: Check Default Selected Value ---
    assert select.first_selected_option.text.strip() == "Active"

    # --- Step 2: Check Option Readability ---
    actual_options = [option.text.strip() for option in select.options]
    assert "Active" in actual_options
    assert "Inactive" in actual_options

    # --- Step 3 & 4: Select INACTIVE via Helper ---
    select_status_inactive(driver)
    assert select.first_selected_option.text.strip() == "Inactive"

    # --- Step 3 & 4: Select ACTIVE via Helper ---
    select_status_active(driver)
    assert select.first_selected_option.text.strip() == "Active"