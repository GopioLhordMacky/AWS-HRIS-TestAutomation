import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_008(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Open 'Add Fiscal Year' modal
        assert page.click_add_fiscal_year_button(), "Failed to click the '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 1: Leave the Start Month empty & Step 2: Click the Save button
        assert page.click_save_only_modal_fiscal_year(), "Failed to click Save button."

        # Expected Result 1: Validation message appears ("Start Date is Required!")
        assert page.check_error_message_fiscal_year("Start Date is Required!"), "Expected validation message 'Start Date is Required!' was not displayed."

        # Expected Result 2: The modal stays open and empty data is not saved
        assert page.is_fiscal_year_modal_visible(), "The modal closed unexpectedly after submitting empty fields."