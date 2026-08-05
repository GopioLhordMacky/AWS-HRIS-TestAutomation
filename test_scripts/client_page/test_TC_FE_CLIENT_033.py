from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_033(authenticated_driver):
    """
    (Accessibility) Verify that Search bar can be navigated and activated using keyboard:
    1. Press Tab until the Search bar is focused.
    2. Input characters into the search bar via keyboard.
    3. Verify typed input is accepted, visible, and table filters properly.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1 & 2: Navigate to the Search bar via tab navigation and trigger search check
    assert KeyboardNavigation.tab_navigation(
        driver,
        locator=Filter_and_Search_Section.SEARCH_BAR,
        helper=TableSearch.check_table_data_by_search,
        column_name="Client Name",
        text="Test"
    ), "Failed to navigate to Search bar using keyboard or search results did not match 'Test'!"

    driver.quit()