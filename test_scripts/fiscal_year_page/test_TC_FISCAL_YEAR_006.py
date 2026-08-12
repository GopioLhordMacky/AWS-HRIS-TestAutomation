import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_006(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Tab until focus reaches 'Add Fiscal Year' button and press ENTER/SPACE
        assert page.tab_navigation_add_fiscal_year(), "Failed to navigate to and activate '+ Add Fiscal Year' button via keyboard."

        # Step 3: Verify the 'Add Fiscal Year' modal opens
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up via keyboard activation."