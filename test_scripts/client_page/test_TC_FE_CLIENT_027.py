from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_027(self, authenticated_driver):
        """
        (Accessibility) Verify Search Bar Accepts Input:
        1. Click into the search bar.
        2. Type alphanumeric characters, special characters, and spaces.
        3. Verify search bar accepts and displays all typed characters correctly.
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # Mixed test string containing alphanumerics, spaces, and special characters
        test_search_input = "Test Client 123!@#"

        # Step 1 & 2: Focus search bar and type test input
        page.search_in_table_client(test_search_input)

        # Step 3: Verify the search bar displays the typed string correctly
        assert page.verify_search_input_matches_client(
            expected_text=test_search_input
        ), f"Search bar did not accept or display the input correctly. Expected: '{test_search_input}'"

    