
from utils.navigation_helpers import go_to_fiscal_year_page
import time

class TestFiscalYearPage:

    def test_tc_fe_client_002(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="sidebar")

        time.sleep(2)

        # Step 1: Click the "+ Add Client" button
        assert  page.click_add_fiscal_year_button(), "Failed to click the '+ Add Client' button on the client page."

        # Step 2: Verify the "Add Client" modal pops up
        assert page.is_fiscal_year_modal_visible(), "The 'Add Client' modal failed to pop up."

        time.sleep(2)

    


