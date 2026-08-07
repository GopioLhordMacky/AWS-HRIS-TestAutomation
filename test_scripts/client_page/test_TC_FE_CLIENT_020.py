from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_020(client_page):
    """Verify Default Selected Value in Industry Dropdown on Clients page."""
    page = client_page

    time.sleep(3)

    # Steps 1-4: Observe Industry dropdown default selection on the main Clients page table filter
    assert page.verify_input_matches(
         
        Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        "All"
    ), "Expected default selected value in Industry dropdown to be 'ALL', but it was not."

    