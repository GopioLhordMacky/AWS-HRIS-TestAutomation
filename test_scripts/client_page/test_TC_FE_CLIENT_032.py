from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_032(authenticated_driver):
    """
    (Functionality) Verify Search Bar Handles No Results:
    1. Enter a random string that does not match any data.
    2. Verify table displays 'No results found'.
    """
    driver= authenticated_driver
    go_to_client_page(driver, via ="url")

    non_existent_keyword = "XYZ_NonExistent_9999!"

    # Single helper call to search and verify empty state
    assert TableSearch.check_table_verify_no_results(
        driver, 
        search_term=non_existent_keyword
    ), f"Expected 'No results found' in table body for search query '{non_existent_keyword}'."

    driver.quit()