import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_016(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Select 'Active' from Status dropdown and verify table contents
        assert page.select_status_filter_fiscal_year("Active"), "Failed to select 'Active' status."
        assert page.check_toggle_status_on_table_fiscal_year("Active", "Active"), (
            "Table did not correctly display Active records."
        )

        # Step 1 & 2: Select 'Inactive' from Status dropdown and verify table contents
        assert page.select_status_filter_fiscal_year("Inactive"), "Failed to select 'Inactive' status."
        assert page.check_toggle_status_on_table_fiscal_year("Active", "Inactive"), (
            "Table did not correctly display Inactive records."
        )