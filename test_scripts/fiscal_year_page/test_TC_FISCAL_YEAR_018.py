import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field,
    verify_table_search_results    
)
from locators import Options, Table

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_018(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    # --- Pre-condition ---
    login_helper(driver)

    # --- Step 1: Reachability - Navigate to Search bar via TAB ---
    actions.send_keys(Keys.TAB).perform()

    search_input_el = wait.until(EC.presence_of_element_located((By.XPATH, Options.SEARCH_FIELD)))
    
    # Fallback to click if focus didn't shift directly
    if driver.switch_to.active_element != search_input_el:
        search_input_el.click()

    # --- Step 2: Populate search field using default string ---
    fill_search_field(driver)

    # --- Step 3: Trigger filtering via ENTER key ---
    search_input_el.send_keys(Keys.ENTER)

    # --- Step 4: Verify table state using new helper ---
    verify_table_search_results(driver)