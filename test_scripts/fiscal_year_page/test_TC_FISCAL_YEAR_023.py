import time
from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field
)
from locators import Table, Confirmation_Dialogue, Buttons, Options
from Fiscal_Year_Page.helper_categ.toggle_helpers import toggle_row_confirm, count_rows
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    change_rows_per_page,
    wait_for_valid_pagination
)

def get_total_count_from_pagination(driver):
    """Extracts the total record count from pagination text (e.g., '1–10 of 21' -> 21)."""
    text = get_pagination_text(driver)
    if "of" in text:
        return int(text.split("of")[-1].strip())
    return count_rows(driver)

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_023(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    login_helper(driver)

    # Force 10 rows per page standard baseline
    change_rows_per_page(driver, 10)

    # 1. Capture Inactive count via pagination total
    select_status(driver, status="Inactive")
    wait_for_valid_pagination(driver)
    initial_total_Inactive = get_total_count_from_pagination(driver)

    # 2. Capture Active count via pagination total
    select_status(driver, status="Active")
    wait_for_valid_pagination(driver)
    initial_total_Active = get_total_count_from_pagination(driver)

    # 3. Switch back to Active and perform Toggle
    select_status(driver, status="Inactive")
    wait_for_valid_pagination(driver)

    toggle_row_confirm(driver)
    wait_for_valid_pagination(driver)

    new_total_active = get_total_count_from_pagination(driver)
    assert new_total_active == initial_total_Inactive - 1, (
        f"Expected Active total to decrease. Initial: {initial_total_Inactive}, New: {new_total_active}"
    )

    # 4. Verify Inactive total increased by 1
    select_status(driver, status="Active")
    wait_for_valid_pagination(driver)

    new_total_inactive = get_total_count_from_pagination(driver)
    assert new_total_inactive == initial_total_Active + 1, (
        f"Expected Inactive total to increase. Initial: {initial_total_Active}, New: {new_total_inactive}"
    )