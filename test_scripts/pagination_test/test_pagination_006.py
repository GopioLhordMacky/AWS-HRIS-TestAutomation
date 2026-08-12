import time
from utils.navigation_helpers import go_to_fiscal_year_page
from selenium.webdriver.common.by import By


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_031(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Perform search to isolate a single page / minimal results
        page.search_fiscal_year("INVALID_!@#123")
        time.sleep(2)

        # Step 2: Capture initial pagination text
        initial_pag_info = page.get_pagination_information_fiscal_year()

        # Step 3: Attempt Next navigation
        try:
            page.go_to_next_page_fiscal_year()
            time.sleep(1)
        except Exception:
            pass  # Expected if button is disabled or unclickable

        after_next_info = page.get_pagination_information_fiscal_year()
        assert after_next_info == initial_pag_info, (
            f"Pagination state changed after clicking Next on a single page! "
            f"Expected '{initial_pag_info}', got '{after_next_info}'."
        )

        # Step 4: Attempt Previous navigation
        try:
            page.go_to_prev_page_fiscal_year()
            time.sleep(1)
        except Exception:
            pass  # Expected if button is disabled or unclickable

        after_prev_info = page.get_pagination_information_fiscal_year()
        assert after_prev_info == initial_pag_info, (
            f"Pagination state changed after clicking Previous on a single page! "
            f"Expected '{initial_pag_info}', got '{after_prev_info}'."
        )
