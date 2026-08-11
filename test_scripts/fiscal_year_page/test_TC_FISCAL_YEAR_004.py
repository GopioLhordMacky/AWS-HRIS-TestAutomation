import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_004(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # 1. Title Check
        assert page.is_page_title_visible(), "Fiscal Year page title is missing or not displayed."

        # 2. Add Fiscal Year Button Check
        assert page.is_add_fiscal_year_button_visible(), "'+ Add Fiscal Year' button is missing or not displayed."

        # 3. Status Label and Dropdown & Search Bar Check
        assert page.is_search_bar_and_dropdown_visible(), "Search bar or Status filter dropdown is missing or not displayed."

        # 4. Table Columns Check
        headers = page.get_table_headers_client()
        expected_columns = [
            "Fiscal Year",
            "FY Code",
            "Start Date",
            "End Date",
            "Date Created",
            "Date Updated",
            "Active",
        ]
        for column in expected_columns:
            assert any(column.lower() in h.lower() for h in headers), f"Column '{column}' missing from table."

        # 5. Pagination Check
        assert page.is_pagination_component_visible(), "Pagination controls are missing or not displayed."