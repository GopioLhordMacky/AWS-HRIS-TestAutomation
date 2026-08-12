from utils.navigation_helpers import go_to_fiscal_year_page
class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_025(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # 1. Assert Rows Per Page Dropdown visibility
        assert page.is_row_per_page_dropdown_visible(), "Failed to find row per page"

        # 2. Assert Pagination Range Information text visibility & non-emptiness
        pag_info = page.get_pagination_information_fiscal_year()
        assert pag_info is not None and len(pag_info) > 0, \
            f"Pagination information text is missing or empty! Got: '{pag_info}'"

        # 3. Assert Next Page Button visibility
        assert page.is_next_page_button_visible(), "Next page button is not visible!"

        # 4. Assert Previous Page Button visibility
        assert page.is_next_prev_button_visible(), "Previous page button is not visible!"

