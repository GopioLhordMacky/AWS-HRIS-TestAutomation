from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_033(self, authenticated_driver):
        """
        (Accessibility) Verify that Search bar can be navigated and activated using keyboard:
        1. Press Tab until the Search bar is focused.
        2. Input characters into the search bar via keyboard.
        3. Verify typed input is accepted, visible, and table filters properly.
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # Step 1 & 2: Navigate to the Search bar via tab navigation and trigger search check
        assert page.tab_navigation_search_bar(
            helper=page.check_table_data_by_search_client,
            column_name="Client Name",
            text="Test"
        ), "Failed to navigate to Search bar using keyboard or search results did not match 'Test'!"

    