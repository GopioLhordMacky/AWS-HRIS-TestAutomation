from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_063(client_page):
    """
    TC_FE_CLIENTS_063: (Accessibility) Verify Pagination Controls keyboard navigation
    
    1. Capture initial page 1 pagination range text.
    2. Use tab_navigation to focus the Next button and press ENTER.
    3. Verify pagination range updates to page 2.
    4. Use tab_navigation to focus the Previous button and press SPACE.
    5. Verify pagination range returns back to page 1.
    """
    page = client_page

    time.sleep(2)

    # Step 1: Record initial pagination state on Page 1
    initial_pag_info = page.get_pagination_information()

    # Step 2: Navigate via TAB to Next button and trigger with ENTER
    page.tab_navigation(
          
        locator=PaginationLocators.NEXT_PAGE_BTN, 
        keys=Keys.ENTER
    )
    time.sleep(1.5)

    # Step 3: Verify page advanced
    next_pag_info = page.get_pagination_information()
    assert next_pag_info != initial_pag_info, (
        f"Keyboard activation via ENTER failed to advance page! "
        f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
    )

    # Step 4: Navigate via TAB to Previous button and trigger with SPACE
    page.tab_navigation(
          
        locator=PaginationLocators.PREV_PAGE_BTN, 
        keys=Keys.SPACE
    )
    time.sleep(1.5)

    # Step 5: Verify page returned to initial range
    prev_pag_info = page.get_pagination_information()
    assert prev_pag_info == initial_pag_info, (
        f"Keyboard activation via SPACE failed to return to previous page! "
        f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
    )

