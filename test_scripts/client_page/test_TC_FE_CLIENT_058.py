from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_058():
    """
    TC_FE_CLIENTS_058: (Functionality) Verify Next and Previous Page Navigation
    
    1. Capture initial page pagination range information (e.g., "1–20 of 113").
    2. Click Next page button using go_to_next_page helper.
    3. Verify pagination range info updates to reflect the next page (e.g., "21–40 of 113").
    4. Click Previous page button using go_to_prev_page helper.
    5. Verify pagination range info returns to the initial range.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Record initial pagination info on Page 1
    time.sleep(3)
    initial_pag_info = get_pagination_information(driver)

    # Step 2: Navigate to Next Page
    go_to_next_page(driver)
    time.sleep(1)

    # Step 3: Capture and verify updated pagination info
    next_pag_info = get_pagination_information(driver)
    assert next_pag_info != initial_pag_info, (
        f"Pagination info did not update after clicking Next! "
        f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
    )

    # Step 4: Navigate back using Previous Page button
    go_to_prev_page(driver)
    time.sleep(3)

    # Step 5: Capture and verify pagination returned to initial state
    prev_pag_info = get_pagination_information(driver)
    assert prev_pag_info == initial_pag_info, (
        f"Pagination info failed to return to initial range after clicking Previous! "
        f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
    )

    close_browser(driver)