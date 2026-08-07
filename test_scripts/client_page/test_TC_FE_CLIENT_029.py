from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_029(client_page):
    """
    (Functionality) Verify Search Bar Clears and Table Resets:
    1. Record initial table count via pagination.
    2. Enter a search term to filter results and record filtered count.
    3. Clear the search bar manually and verify table resets back to initial state.
    """
    page = client_page


    # Step 1: Wait for initial table load and record initial pagination info
    time.sleep(3)
    initial_pagination = page.get_pagination_information()
    
    # Step 2: Search for a term to filter the table
    search_term = "test"
    page.search_in_table(  search_term)
    time.sleep(3)
    
    searched_pagination = page.get_pagination_information()

    # Assert that the search actually filtered the table (counts should not be equal)
    assert initial_pagination != searched_pagination, (
        f"Search term '{search_term}' did not change table results! "
        f"Initial: {initial_pagination}, Searched: {searched_pagination}"
    )

    # Step 3: Clear the search term
    page.clear_input_field(  Filter_and_Search_Section.SEARCH_BAR)
    time.sleep(3)

    cleared_pagination = page.get_pagination_information()

    # Step 4: Verify the table resets back to the initial unfiltered state
    assert cleared_pagination == initial_pagination, (
        f"Table failed to reset after clearing search bar! "
        f"Expected initial: {initial_pagination}, Got: {cleared_pagination}"
    )

    