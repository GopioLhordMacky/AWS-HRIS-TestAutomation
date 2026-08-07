from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_032(client_page):
    """
    (Functionality) Verify Search Bar Handles No Results:
    1. Enter a random string that does not match any data.
    2. Verify table displays 'No results found'.
    """
    page = client_page
    
    non_existent_keyword = "XYZ_NonExistent_9999!"

    # Single helper call to search and verify empty state
    assert page.check_table_verify_no_results(
          
        search_term=non_existent_keyword
    ), f"Expected 'No results found' in table body for search query '{non_existent_keyword}'."

    