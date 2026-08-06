from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_062(authenticated_driver):
    """
    TC_FE_CLIENTS_062: (Functionality) Verify Pagination with single page
    
    1. Filter table using search term "INVALID_!@#123" so that results fit on a single page (0 or 1 page).
    2. Capture initial pagination info string.
    3. Attempt to navigate Next and Previous.
    4. Assert that the pagination text string remains completely unchanged (confirming non-functionality/single-page boundary).
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Perform search to isolate a single page / minimal results
    TableSearch.search_in_table(driver, "INVALID_!@#123")
    time.sleep(2)

    # Step 2: Capture initial pagination text
    initial_pag_info = TablePagination.get_pagination_information(driver)

    # Step 3: Attempt Next navigation
    try:
        TablePagination.go_to_next_page(driver)
        time.sleep(1)
    except Exception:
        pass  # Expected if button is disabled or unclickable

    after_next_info = TablePagination.get_pagination_information(driver)
    assert after_next_info == initial_pag_info, (
        f"Pagination state changed after clicking Next on a single page! "
        f"Expected '{initial_pag_info}', got '{after_next_info}'."
    )

    # Step 4: Attempt Previous navigation
    try:
        TablePagination.go_to_prev_page(driver)
        time.sleep(1)
    except Exception:
        pass  # Expected if button is disabled or unclickable

    after_prev_info = TablePagination.get_pagination_information(driver)
    assert after_prev_info == initial_pag_info, (
        f"Pagination state changed after clicking Previous on a single page! "
        f"Expected '{initial_pag_info}', got '{after_prev_info}'."
    )
