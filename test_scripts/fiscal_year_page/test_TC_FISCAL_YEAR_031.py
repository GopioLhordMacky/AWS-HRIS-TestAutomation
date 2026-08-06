import time
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    get_displayed_row_count,
    is_button_disabled,
    change_rows_per_page
)
from helpers import *
from locators import Pagination

@pytest.mark.performance
def test_TC_FE_FISCAL_YEAR_031(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    
    # Apply search keyword to yield a small dataset (1 page only)
    fill_search_field(driver, search_str="202")
    time.sleep(2)

    # Force 10 rows per page to evaluate under standard base limit
    change_rows_per_page(driver, 10)
    time.sleep(1)

    # --- Step 1: Verify Next/Prev buttons are disabled or not navigable ---
    prev_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON))
    )
    next_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.NEXT_PAGE_BUTTON))
    )

    # Verify Previous (<) button is disabled
    assert is_button_disabled(prev_btn), (
        "Expected Previous ('<') button to be disabled for single-page results."
    )

    # Verify Next (>) button is disabled
    assert is_button_disabled(next_btn), (
        "Expected Next ('>') button to be disabled when all results fit on a single page."
    )

    # --- Step 2: Verify table displays all rows correctly ---
    displayed_rows = get_displayed_row_count(driver)
    pagination_text = get_pagination_text(driver)

    # Ensure at least 1 row exists for a valid small search result
    assert displayed_rows > 0, (
        f"Expected at least 1 record for search '202', but found {displayed_rows} rows."
    )

    # Verify pagination range text matches total row count (e.g., '1–3 of 3')
    # Extract total count after "of"
    if "of" in pagination_text:
        total_count = int(pagination_text.split("of")[-1].strip())
        assert displayed_rows == total_count, (
            f"Expected displayed row count ({displayed_rows}) to equal total count ({total_count})."
        )