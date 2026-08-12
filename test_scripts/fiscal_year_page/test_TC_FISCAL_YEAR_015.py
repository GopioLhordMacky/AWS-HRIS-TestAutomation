import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_015(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Press TAB until the Status dropdown is focused
        assert page.tab_navigation_status_filter_fiscal_year(), "Failed to navigation and select on Status Filter"

        time.sleep(1)

        # Expected Result: Selected option updates correctly and value reflects "Not Active"
        assert page.select_status_filter_fiscal_year("Active"), "Failed to select status"
        assert page.check_toggle_status_on_table_fiscal_year("Active", "Active"), "Failed to check toggle status on table"
        assert page.verify_status_input_matches_fiscal_year(expected_text="Active"), (
            "Status filter value did not update to 'Not Active' after keyboard selection."
        )