from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_clients_057(client_page):
    """
    TC_FE_CLIENTS_057: (Functionality) Verify Pagination controls visibility
    
    1. Navigate to Clients page.
    2. Verify visibility of the Rows Per Page dropdown.
    3. Verify visibility and non-empty content of the Pagination Information text.
    4. Verify visibility of Next and Previous pagination navigation buttons.
    """
    page = client_page

    # 1. Assert Rows Per Page Dropdown visibility
    assert page.is_component_visible(PaginationLocators.ROWS_PER_PAGE_DROPDOWN), \
        "Rows per page dropdown is not visible!"

    # 2. Assert Pagination Range Information text visibility & non-emptiness
    pag_info = page.get_pagination_information()
    assert pag_info is not None and len(pag_info) > 0, \
        f"Pagination information text is missing or empty! Got: '{pag_info}'"

    # 3. Assert Next Page Button visibility
    assert page.is_component_visible(PaginationLocators.NEXT_PAGE_BTN), \
        "Next page button is not visible!"

    # 4. Assert Previous Page Button visibility
    assert page.is_component_visible(PaginationLocators.PREV_PAGE_BTN), \
        "Previous page button is not visible!"

