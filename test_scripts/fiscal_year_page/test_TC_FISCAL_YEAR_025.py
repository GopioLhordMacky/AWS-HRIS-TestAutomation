import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_025(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        page.select_status_filter_fiscal_year("Inactive")

        # Step 1 & 2: Navigate to toggle button via TAB and trigger via SPACE key
        assert page.tab_navigation_toggle_status(), "Failed to reach and activate toggle button via keyboard TAB."

        assert page.check_toast_message_fiscal_year("The fiscal year is set to active"), (
            "Expected status update success toast was not displayed."
        )