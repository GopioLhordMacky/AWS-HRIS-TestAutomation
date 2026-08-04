from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_061():
    """
    TC_FE_CLIENTS_061: (Functionality) Verify Pagination works correctly with filtered/search results
    
    1. Enter "Test" in the search input field.
    2. Traverse forward using go_to_next_page until the pagination text no longer changes (end of results).
    3. Traverse backward using go_to_prev_page until returning to the initial page 1 range.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Perform search for "Test"
    search_in_table(driver, "Test")
    time.sleep(1.5)  # Allow search filter to apply to grid

    # Capture baseline pagination info for Page 1 of search results
    initial_pag_info = get_pagination_information(driver)

    # Step 2: Traverse forward to the last page
    while True:
        current_info = get_pagination_information(driver)
        
        try:
            go_to_next_page(driver)
            time.sleep(1.5)
        except Exception:
            # Reached end if Next is non-interactable or fails
            break

        updated_info = get_pagination_information(driver)

        # If pagination string text hasn't changed after click, we reached the end
        if current_info == updated_info:
            break

    # Step 3: Traverse backward to return to the first page
    while True:
        current_info = get_pagination_information(driver)

        # Stop if we have returned to the initial starting range (Page 1)
        if current_info == initial_pag_info:
            break

        try:
            go_to_prev_page(driver)
            time.sleep(1.5)
        except Exception:
            # Reached beginning if Prev is non-interactable or fails
            break

        updated_info = get_pagination_information(driver)

        # If pagination string text hasn't changed, we are back at page 1
        if current_info == updated_info:
            break

    # Step 4: Final verification that we returned back to page 1
    final_pag_info = get_pagination_information(driver)
    assert final_pag_info == initial_pag_info, (
        f"Failed end-to-end pagination traversal! "
        f"Expected to return to '{initial_pag_info}', but stopped at '{final_pag_info}'."
    )

    close_browser(driver)