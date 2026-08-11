from utils.navigation_helpers import go_to_fiscal_year_page
import time

class TestFiscalYearPage:

    def test_tc_fe_client_003(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        is_clean, errors = page.check_console_error_fiscal_year()

        # Checks for errors, prints them if present, and asserts result
        assert is_clean, f"Console error test failed! Errors found: {errors}"

    
