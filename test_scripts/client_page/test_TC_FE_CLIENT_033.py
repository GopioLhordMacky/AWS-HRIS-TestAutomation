from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_033():
    """
    (Accessibility) Verify that Search bar can be navigated and activated using keyboard:
    1. Press Tab until the Search bar is focused.
    2. Input characters into the search bar via keyboard.
    3. Verify typed input is accepted, visible, and table filters properly.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1 & 2: Navigate to the Search bar via tab navigation and trigger search check
    assert tab_navigation(
        driver,
        locator=Filter_and_Search_Section.SEARCH_BAR,
        helper=check_table_data_by_search,
        column_name="Client Name",
        text="Test"
    ), "Failed to navigate to Search bar using keyboard or search results did not match 'Test'!"

    close_browser(driver)