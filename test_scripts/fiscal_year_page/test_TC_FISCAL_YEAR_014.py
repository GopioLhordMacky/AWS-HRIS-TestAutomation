import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_014(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 5: Verify default selected value is "Active"
        assert page.verify_status_input_matches_fiscal_year(expected_text="Active"), (
            "Default status filter value is not 'Active'."
        )

        # Step 1, 2 & Expected 1, 2: Verify Status dropdown options list match expected values
        assert page.verify_status_dropdown_options_fiscal_year(), (
            "Status dropdown options do not match the expected list ('Active', 'Inactive')."
        )

        # Step 3, 4: Select an option (e.g., 'Inactive') and verify value updates
        assert page.select_status_filter_fiscal_year("Inactive"), "Failed to select 'Inactive' from Status dropdown."
        time.sleep(1)
        assert page.verify_status_input_matches_fiscal_year(expected_text="Not Active"), (
            "Status filter value did not update to 'Inactive' after selection."
        )