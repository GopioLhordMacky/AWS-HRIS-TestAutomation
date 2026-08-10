from utils.navigation_helpers import go_to_client_page


class TestClientPage:

    def test_tc_fe_clients_028(self, authenticated_driver):
        """
        (Functionality) Verify that the table updates based on the search bar keyword
        across multiple columns (Client Name, Country, Contact Person).
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Define test data pairs: (search_keyword, target_column)
        search_test_cases = [
            ("test", "Client Name"),
            ("Philippines", "Country"),
            ("John Doe", "Contact Person")
        ]

        for search_keyword, target_column in search_test_cases:
            assert page.check_table_data_by_search_client(
                column_name=target_column,
                text=search_keyword
            ), f"Search failed for keyword '{search_keyword}' under column '{target_column}'!"

    