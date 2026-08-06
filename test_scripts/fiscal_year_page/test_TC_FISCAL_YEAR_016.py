import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from helpers import setup_browser, login_helper
from locators import Options, Table


@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_015(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # Grab the status dropdown element
    dropdown_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.STATUS_DROPDOWN)))
    select = Select(dropdown_el)

    # --- Step 1 & 2: Focus the dropdown via click/focus ---
    dropdown_el.click()  # Focuses and opens/activates the select dropdown via keyboard interaction

    # --- Step 3 & 4: Select 'Inactive' using Keyboard Arrow Keys ---
    dropdown_el.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    # Wait and verify selection changed to Inactive
    wait.until(lambda d: select.first_selected_option.text.strip() == "Inactive")
    assert select.first_selected_option.text.strip() == "Inactive", \
        "Failed to select 'Inactive' via keyboard navigation."

    # Verify table row container responds after filtering
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))

    # --- Step 3 & 4: Select 'Active' using Keyboard Arrow Keys ---
    dropdown_el.send_keys(Keys.ARROW_UP, Keys.ENTER)

    # Wait and verify selection changed back to Active
    wait.until(lambda d: select.first_selected_option.text.strip() == "Active")
    assert select.first_selected_option.text.strip() == "Active", \
        "Failed to select 'Active' via keyboard navigation."

    # Verify table row container responds after filtering
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))