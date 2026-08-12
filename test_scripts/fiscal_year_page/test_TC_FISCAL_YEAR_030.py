import time
from utils.navigation_helpers import go_to_fiscal_year_page
from selenium.webdriver.common.by import By


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_030(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Perform search for "Test"
        page.search_fiscal_year("Test")
        time.sleep(1.5)  # Allow search filter to apply to grid

        # Capture baseline pagination info for Page 1 of search results
        initial_pag_info = page.get_pagination_information_fiscal_year()

        # Step 2: Traverse forward to the last page
        while True:
            current_info = page.get_pagination_information_fiscal_year()
            
            try:
                page.go_to_next_page_fiscal_year()
                time.sleep(1.5)
            except Exception:
                # Reached end if Next is non-interactable or fails
                break

            updated_info = page.get_pagination_information_fiscal_year()

            # If pagination string text hasn't changed after click, we reached the end
            if current_info == updated_info:
                break

        # Step 3: Traverse backward to return to the first page
        while True:
            current_info = page.get_pagination_information_fiscal_year()

            # Stop if we have returned to the initial starting range (Page 1)
            if current_info == initial_pag_info:
                break

            try:
                page.go_to_prev_page_fiscal_year()
                time.sleep(1.5)
            except Exception:
                # Reached beginning if Prev is non-interactable or fails
                break

            updated_info = page.get_pagination_information_fiscal_year()

            # If pagination string text hasn't changed, we are back at page 1
            if current_info == updated_info:
                break

        # Step 4: Final verification that we returned back to page 1
        final_pag_info = page.get_pagination_information_fiscal_year()
        assert final_pag_info == initial_pag_info, (
            f"Failed end-to-end pagination traversal! "
            f"Expected to return to '{initial_pag_info}', but stopped at '{final_pag_info}'."
        )

        