import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_018(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 to 4: Tab navigate to the search bar, enter keyword 'DX', press ENTER, and filter
        assert page.tab_navigation_search_bar(), "Failed to navigate to Search bar using TAB key."

        # Verify search results updated accordingly for 'DX'
        assert page.check_table_data_by_search_fiscal_year("FY Code", "2026"), (
            "Table failed to filter results properly after keyboard search for 'DX'."
        )

        assert page.clear_search_bar(), "Failed to clear input field"
        
        # Verify invalid search via keyboard shows empty state
        assert page.check_table_verify_no_results_fiscal_year("TESTING"), (
            "Table failed to show 'No results found' after searching 'TESTING' via keyboard."
        )