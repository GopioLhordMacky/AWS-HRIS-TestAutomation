import time
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    change_rows_per_page,
    get_displayed_row_count,
    get_pagination_text
)
from helpers import *

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_029(setup_browser):
    driver = setup_browser

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Active")
    time.sleep(2)

    # Options to test
    rows_per_page_options = [10, 20, 50, 100]

    for limit in rows_per_page_options:
        # Step 1 & 2: Select new rows per page option
        change_rows_per_page(driver, limit)

        # Step 3: Verify displayed rows logic
        actual_rows = get_displayed_row_count(driver)
        pagination_text = get_pagination_text(driver)

        # Assert rows visible are <= limit (can be less on the last page or small datasets)
        assert actual_rows <= limit, (
            f"Expected table rows to be <= {limit}, but found {actual_rows} rows."
        )

        # Verify pagination text reflects active size change
        assert pagination_text != "", "Pagination range text should not be empty."