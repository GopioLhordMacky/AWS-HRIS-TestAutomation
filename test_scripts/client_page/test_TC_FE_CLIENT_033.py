from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


def test_tc_fe_clients_033(client_page):
    """
    (Accessibility) Verify that Search bar can be navigated and activated using keyboard:
    1. Press Tab until the Search bar is focused.
    2. Input characters into the search bar via keyboard.
    3. Verify typed input is accepted, visible, and table filters properly.
    """
    page = client_page


    # Step 1 & 2: Navigate to the Search bar via tab navigation and trigger search check
    assert page.tab_navigation(
         
        locator=Filter_and_Search_Section.SEARCH_BAR,
        helper=page.check_table_data_by_search,
        column_name="Client Name",
        text="Test"
    ), "Failed to navigate to Search bar using keyboard or search results did not match 'Test'!"

    