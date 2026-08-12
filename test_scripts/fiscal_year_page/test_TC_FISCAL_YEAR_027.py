import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_027(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Record initial pagination info on Page 1
        time.sleep(3)
        initial_pag_info = page.get_pagination_information_fiscal_year()

        # Step 2: Navigate to Next Page
        page.go_to_next_page_fiscal_year()
        time.sleep(1)

        # Step 3: Capture and verify updated pagination info
        next_pag_info = page.get_pagination_information_fiscal_year()
        assert next_pag_info != initial_pag_info, (
            f"Pagination info did not update after clicking Next! "
            f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
        )

        # Step 4: Navigate back using Previous Page button
        page.go_to_prev_page_fiscal_year()
        time.sleep(3)

        # Step 5: Capture and verify pagination returned to initial state
        prev_pag_info = page.get_pagination_information_fiscal_year()
        assert prev_pag_info == initial_pag_info, (
            f"Pagination info failed to return to initial range after clicking Previous! "
            f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
        )

        # Step 1: Record initial pagination info on Page 1
        time.sleep(3)
        initial_pag_info = page.get_pagination_information_fiscal_year()

        # Step 2: Navigate to Next Page
        page.go_to_next_page_fiscal_year()
        time.sleep(1)

        # Step 3: Capture and verify updated pagination info
        next_pag_info = page.get_pagination_information_fiscal_year()
        assert next_pag_info != initial_pag_info, (
            f"Pagination info did not update after clicking Next! "
            f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
        )

        # Step 4: Navigate back using Previous Page button
        page.go_to_prev_page_fiscal_year()
        time.sleep(3)

        # Step 5: Capture and verify pagination returned to initial state
        prev_pag_info = page.get_pagination_information_fiscal_year()
        assert prev_pag_info == initial_pag_info, (
            f"Pagination info failed to return to initial range after clicking Previous! "
            f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
        )

