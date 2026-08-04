from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_057():
    """
    TC_FE_CLIENTS_057: (Functionality) Verify Pagination controls visibility
    
    1. Navigate to Clients page.
    2. Verify visibility of the Rows Per Page dropdown.
    3. Verify visibility and non-empty content of the Pagination Information text.
    4. Verify visibility of Next and Previous pagination navigation buttons.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # 1. Assert Rows Per Page Dropdown visibility
    assert is_component_visible(driver, PaginationLocators.ROWS_PER_PAGE_DROPDOWN), \
        "Rows per page dropdown is not visible!"

    # 2. Assert Pagination Range Information text visibility & non-emptiness
    pag_info = get_pagination_information(driver)
    assert pag_info is not None and len(pag_info) > 0, \
        f"Pagination information text is missing or empty! Got: '{pag_info}'"

    # 3. Assert Next Page Button visibility
    assert is_component_visible(driver, PaginationLocators.NEXT_PAGE_BTN), \
        "Next page button is not visible!"

    # 4. Assert Previous Page Button visibility
    assert is_component_visible(driver, PaginationLocators.PREV_PAGE_BTN), \
        "Previous page button is not visible!"

    close_browser(driver)