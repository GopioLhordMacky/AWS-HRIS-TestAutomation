from locators.client_page_locators import Filter_and_Search_Section
from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_029(self, authenticated_driver):
        """
        (Functionality) Verify Search Bar Clears and Table Resets:
        1. Record initial table count via pagination.
        2. Enter a search term to filter results and record filtered count.
        3. Clear the search bar manually and verify table resets back to initial state.
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # Step 1: Wait for initial table load and record initial pagination info
        time.sleep(2)
        initial_pagination = page.get_pagination_information_client()
        
        # Step 2: Search for a term to filter the table
        search_term = "test"
        page.search_in_table_client(search_term)
        time.sleep(2)
        
        searched_pagination = page.get_pagination_information_client()

        # Assert that the search actually filtered the table (counts should not be equal)
        assert initial_pagination != searched_pagination, (
            f"Search term '{search_term}' did not change table results! "
            f"Initial: {initial_pagination}, Searched: {searched_pagination}"
        )

        # Step 3: Clear the search term
        page.clear_search_bar()
        time.sleep(2)
        cleared_pagination = page.get_pagination_information_client()

        # Step 4: Verify the table resets back to the initial unfiltered state
        assert cleared_pagination == initial_pagination, (
            f"Table failed to reset after clearing search bar! "
            f"Expected initial: {initial_pagination}, Got: {cleared_pagination}"
        )

        