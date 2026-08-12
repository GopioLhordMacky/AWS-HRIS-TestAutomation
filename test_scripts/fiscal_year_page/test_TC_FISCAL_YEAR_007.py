import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_007(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Open 'Add Fiscal Year' modal and verify it pops up
        assert page.click_add_fiscal_year_button(), "Failed to click the '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 3: Verify Modal UI Components
        # - Modal Title
        assert page.is_modal_title_visible(), "Modal title is missing or not displayed."

        # - Verify all input fields (Start Date, End Date, FY Name, FY Code) are present
        assert page.is_fiscal_year_modal_inputs_visible(), "One or more modal input fields are missing."

        # - Verify disabled fields (End Date, FY Name, FY Code)
        assert page.are_read_only_fields_disabled(), "One or more calculated/read-only fields are not disabled."

        # - Verify Modal Action Buttons (Close and Save)
        assert page.is_fiscal_year_modal_buttons_visible(), "Modal Close or Save buttons are missing."