import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_005(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Click the "+ Add Fiscal Year" button
        assert page.click_add_fiscal_year_button(), "Failed to click the '+ Add Fiscal Year' button."

        # Step 2: Verify the 'Add Fiscal Year' modal pops up
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."