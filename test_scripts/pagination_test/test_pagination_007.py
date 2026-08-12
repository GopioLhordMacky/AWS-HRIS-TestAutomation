import time
from utils.navigation_helpers import go_to_fiscal_year_page
from selenium.webdriver.common.by import By


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_031(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        time.sleep(2)

        # Step 1: Record initial pagination state on Page 1
        initial_pag_info = page.get_pagination_information_fiscal_year()

        # Step 2: Navigate via TAB to Next button and trigger with ENTER
        page.tab_navigation_next_btn()
        time.sleep(1.5)

        # Step 3: Verify page advanced
        next_pag_info = page.get_pagination_information_fiscal_year()
        assert next_pag_info != initial_pag_info, (
            f"Keyboard activation via ENTER failed to advance page! "
            f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
        )

        # Step 4: Navigate via TAB to Previous button and trigger with SPACE
        page.tab_navigation_prev_btn()
        time.sleep(1.5)

        # Step 5: Verify page returned to initial range
        prev_pag_info = page.get_pagination_information_fiscal_year()
        assert prev_pag_info == initial_pag_info, (
            f"Keyboard activation via SPACE failed to return to previous page! "
            f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
        )

