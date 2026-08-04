from helpers.client_page_helpers import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *


class TestClient004:

    @pytest.mark.passed
    def test_tc_fe_clients_004(self):
        """Verify UI design and presence of mandatory components on Clients Module."""
        driver = open_browser("chrome")
        login_client_page(driver)
        time.sleep(2)

       #1. Title & Core Table
        assert is_client_page_loaded(driver), "Title or Table is missing."

        # 2. Add Client Button & Search Bar
        assert is_component_clickable(driver, Client_Locators.ADD_CLIENT_BUTTON, timeout=10), "Add Client button missing."
        assert is_component_visible(driver, Filter_and_Search_Section.SEARCH_BAR), "Search bar missing."

        # 3. Dropdowns (Industry, Status, Rows per page)
        assert is_component_visible(driver, Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN), "Industry dropdown missing."
        assert is_component_visible(driver, Filter_and_Search_Section.STATUS_FILTER_DROPDOWN), "Status dropdown missing."

        # 4. Table Columns Check
        headers = get_table_headers(driver)
        expected_columns = ["Client Name", "Industry", "Country", "Contact Person", "Active"]
        for column in expected_columns:
            assert any(column.lower() in h.lower() for h in headers), f"Column '{column}' missing from table."

        # 5. Pagination Component Check
        assert is_component_visible(driver, Pagination_Section.PAGINATION_CONTAINER), "Pagination component missing."

        close_browser(driver)

if __name__ == "__main__":
    TestClient004().test_tc_fe_clients_004()