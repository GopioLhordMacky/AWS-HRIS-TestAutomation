import time
from plugins import *
from helpers import setup_browser, login_helper, select_status
from locators import Pagination

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_026(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Active")
    time.sleep(2)

    # --- Step 1: Locate and verify Pagination components ---
    
    # 1. Rows per page dropdown
    dropdown = wait.until(
        EC.visibility_of_element_located((By.XPATH, Pagination.ROWS_PER_PAGE_DROPDOWN))
    )
    assert dropdown.is_displayed(), "Expected 'Rows per page' dropdown to be visible."

    # 2. Page range text (e.g., "1–10 of 14")
    displayed_rows = wait.until(
        EC.visibility_of_element_located((By.XPATH, Pagination.DISPLAYED_ROWS_TEXT))
    )
    assert displayed_rows.is_displayed(), "Expected displayed rows page range text to be visible."
    assert "of" in displayed_rows.text, f"Expected range format like 'XX-XX of XXX', but got '{displayed_rows.text}'"

    # 3. Previous (<) page button
    prev_button = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON))
    )
    assert prev_button.is_displayed(), "Expected Previous page button to be visible."

    # 4. Next (>) page button
    next_button = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.NEXT_PAGE_BUTTON))
    )
    assert next_button.is_displayed(), "Expected Next page button to be visible."