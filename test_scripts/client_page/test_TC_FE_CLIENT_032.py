from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_032(self, authenticated_driver):
        """
        (Functionality) Verify Search Bar Handles No Results:
        1. Enter a random string that does not match any data.
        2. Verify table displays 'No results found'.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        non_existent_keyword = "XYZ_NonExistent_9999!"

        # Single helper call to search and verify empty state
        assert page.check_table_verify_no_results_client(
            search_term=non_existent_keyword
        ), f"Expected 'No results found' in table body for search query '{non_existent_keyword}'."

    