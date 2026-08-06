import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field
)
from locators import Options, Table

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_017(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # --- Step 1: Select Status using helper defaults ---
    select_status(driver)

    # --- Step 2: Fill Search using helper defaults ---
    fill_search_field(driver)

    # Retrieve whatever search string was typed into the input field
    search_input_el = wait.until(EC.element_to_be_clickable((By.XPATH, Options.SEARCH_FIELD)))
    current_search_term = search_input_el.get_attribute("value").strip()

    # --- Step 3: Assert Table State (Data Rows OR Empty State) ---
    wait.until(
        lambda d: current_search_term in d.find_element(By.XPATH, Table.BODY).text
        or "no results found" in d.find_element(By.XPATH, Table.BODY).text.lower()
    )

    body_text = driver.find_element(By.XPATH, Table.BODY).text

    if "no results found" in body_text.lower():
        # Passed empty state check
        assert True
    else:
        # Validate that EVERY visible row contains the search input value
        rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
        assert len(rows) > 0, f"Expected table rows for search query '{current_search_term}'."
        for row in rows:
            assert current_search_term in row.text, (
                f"Row text '{row.text}' did not contain the search input value '{current_search_term}'."
            )