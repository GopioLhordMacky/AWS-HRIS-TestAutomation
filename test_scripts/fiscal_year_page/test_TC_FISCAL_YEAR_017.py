import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_017(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Search for an invalid keyword (e.g., 'DX') and assert 'No results found'
        assert page.check_table_verify_no_results_fiscal_year("DX"), (
            "Expected 'No results found' message was not displayed for invalid keyword 'TESTING'."
        )