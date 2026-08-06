from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_059(authenticated_driver):
    """
    TC_FE_CLIENTS_059: (Functionality) Verify Previous and Next buttons are disabled on first and last pages
    
    1. Navigate to Clients page (default page 1).
    2. Assert Previous button is disabled on page 1.
    3. Loop using go_to_next_page(driver) until pagination range no longer changes.
    4. Assert Next button is disabled on the final page.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Check Previous button state on First Page
    prev_btn = driver.find_element(*PaginationLocators.PREV_PAGE_BTN)
    assert not prev_btn.is_enabled() or prev_btn.get_attribute("disabled") is not None, \
        "Previous page button should be disabled on the first page!"

    # Step 2: Navigate to Last Page by observing text updates
    while True:
        current_info = TablePagination.get_pagination_information(driver)
        
        try:
            TablePagination.go_to_next_page(driver)
            time.sleep(1.5)
        except Exception:
            # If wait_for_and_click fails because the button became unclickable/disabled, we've hit the end
            break

        updated_info = TablePagination.get_pagination_information(driver)

        # If pagination range text didn't change after clicking, we are on the last page
        if current_info == updated_info:
            break

    # Step 3: Check Next button state on Last Page
    next_btn = driver.find_element(*PaginationLocators.NEXT_PAGE_BTN)
    assert not next_btn.is_enabled() or next_btn.get_attribute("disabled") is not None, \
        "Next page button should be disabled on the last page!"

