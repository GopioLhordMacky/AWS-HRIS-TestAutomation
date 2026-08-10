from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_004(self, authenticated_driver):
        """Verify UI design and presence of mandatory components on Clients Module."""

        page = go_to_client_page(authenticated_driver, via="url")

        # 2. Add Client Button
        assert page.is_add_client_button_visible(), "Add Client button missing."

        # 3. Dropdowns and Search Bar Check
        assert page.is_search_bar_and_dropdown_visible(), "Search bar or dropdowns missing."

        # 4. Table Columns Check
        headers = page.get_table_header_clients()
        expected_columns = ["Client Name", "Industry", "Country", "Contact Person", "Active"]
        for column in expected_columns:
            assert any(column.lower() in h.lower() for h in headers), f"Column '{column}' missing from table."

        # 5. Pagination Component Check
        assert page.is_pagination_component_visible(), "Pagination component missing."