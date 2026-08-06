import time
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    go_to_next_page,
    go_to_previous_page,
    get_first_row_text,
    click_page_number,
    is_page_selected,
    change_rows_per_page
)
from helpers import *


def wait_for_valid_pagination(driver, timeout=10):
    """Waits until pagination text is loaded and not showing temporary '0–0 of 0' state."""
    wait = WebDriverWait(driver, timeout)
    wait.until(
        lambda d: get_pagination_text(d) != "0–0 of 0" and get_pagination_text(d) != ""
    )

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_030(setup_browser):
    driver = setup_browser

    # --- Pre-condition ---
    login_helper(driver)
    
    # Step 1: Apply filter (Status: "Active")
    select_status(driver, status="Inactive")
    # fill_search_field(driver, search_str="202")
    time.sleep(2)
    change_rows_per_page(driver)
    wait_for_valid_pagination(driver)

    # Capture filtered initial state (Page 1)
    filtered_p1_text = get_pagination_text(driver)
    filtered_p1_row = get_first_row_text(driver)

    # Step 2: Click Next (>) button on filtered results
    go_to_next_page(driver)
    wait_for_valid_pagination(driver)
    
    filtered_p2_text = get_pagination_text(driver)
    filtered_p2_row = get_first_row_text(driver)

    # Assert filtered data updated on Next
    assert filtered_p2_text != filtered_p1_text, (
        "Expected range text to update on filtered results after clicking Next."
    )
    assert filtered_p2_row != filtered_p1_row, (
        "Expected row data to update on filtered results after clicking Next."
    )

    # Step 3: Click Prev (<) button on filtered results
    go_to_previous_page(driver)
    wait_for_valid_pagination(driver)

    returned_p1_text = get_pagination_text(driver)
    returned_p1_row = get_first_row_text(driver)

    # Assert filtered data reverted on Previous
    assert returned_p1_text == filtered_p1_text, (
        f"Expected range to revert to '{filtered_p1_text}', but got '{returned_p1_text}'."
    )
    assert returned_p1_row == filtered_p1_row, (
        "Expected table content to revert back to initial filtered Page 1 data."
    )

