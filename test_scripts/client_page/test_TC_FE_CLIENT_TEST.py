from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

class TestClientPage: 

    def test_tc_fe_clients_004(self, authenticated_driver):
        """Verify UI design and presence of mandatory components on Clients Module."""
        page = go_to_client_page (authenticated_driver, via="url")
        
        # 1. Title & Core Table Check
        # 2. Add Client Button & Search Bar Check
        assert page.ensure_element_visible(Client_Locators.ADD_CLIENT_BUTTON), "Add Client button missing."
        assert page.ensure_element_visible(Filter_and_Search_Section.SEARCH_BAR), "Search bar missing."

        # 3. Dropdowns Check
        assert page.ensure_element_visible(Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN), "Industry dropdown missing."
        assert page.ensure_element_visible(Filter_and_Search_Section.STATUS_FILTER_DROPDOWN), "Status dropdown missing."

        # 4. Table Columns Check
        headers = page.get_table_headers_client()
        expected_columns = ["Client Name", "Industry", "Country", "Contact Person", "Active"]
        for column in expected_columns:
            assert any(column.lower() in h.lower() for h in headers), f"Column '{column}' missing from table."

        # 5. Pagination Component Check
        assert page.ensure_element_visible(Pagination_Section.PAGINATION_CONTAINER), "Pagination component missing."