import time
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    go_to_next_page,
    go_to_previous_page,
    get_first_row_text,
    change_rows_per_page,
    wait_for_valid_pagination
)
from helpers import *

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_027(setup_browser):
    driver = setup_browser

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(5)
    
    # Standardize baseline rows per page & wait for table to settle
    change_rows_per_page(driver, 10)
    wait_for_valid_pagination(driver)

    # Capture Page 1 initial state
    initial_page_text = get_pagination_text(driver)
    initial_first_row = get_first_row_text(driver)

    # --- Step 1 & 2: Click Next (>) and verify updates ---
    go_to_next_page(driver)
    wait_for_valid_pagination(driver)
    
    page2_text = get_pagination_text(driver)
    page2_first_row = get_first_row_text(driver)

    # Assert range text changed
    assert page2_text != initial_page_text, (
        f"Expected page range text to change on Next page, but remained '{initial_page_text}'"
    )

    # Assert row content updated
    assert page2_first_row != initial_first_row, (
        "Expected first row record to update after navigating to Next page."
    )

    # --- Step 3 & 4: Click Previous (<) and verify returning to Page 1 ---
    go_to_previous_page(driver)
    wait_for_valid_pagination(driver)

    page1_returned_text = get_pagination_text(driver)
    page1_returned_first_row = get_first_row_text(driver)

    # Assert returned range matches initial Page 1 range
    assert page1_returned_text == initial_page_text, (
        f"Expected pagination range to return to '{initial_page_text}', but got '{page1_returned_text}'"
    )

    # Assert row content matches initial Page 1 row
    assert page1_returned_first_row == initial_first_row, (
        "Expected table content to revert back to initial Page 1 records."
    )