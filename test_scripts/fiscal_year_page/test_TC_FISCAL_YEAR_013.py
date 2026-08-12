import time
from data.fiscal_year_page_inputs import FillStartDate
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_013(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")
        start_data = FillStartDate()

        # --- CYCLE 1: Close via "Close" button ---
        # Step 1: Click '+ Add Fiscal Year' button to open modal
        assert page.click_add_fiscal_year_button(), "Failed to click '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 2: Select Start Date
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 3: Close modal using Close button
        assert page.click_close_modal_fiscal_year(), "Failed to click Close button on modal."
        time.sleep(1)
        assert not page.is_fiscal_year_modal_visible(), "Modal was not closed after clicking Close button."

        # Step 4 & 5: Reopen modal and verify fields are cleared
        assert page.click_add_fiscal_year_button(), "Failed to reopen '+ Add Fiscal Year' modal."
        assert page.is_fiscal_year_modal_visible(), "Modal failed to display upon reopening."
        assert page.verify_modal_fields_are_cleared(), "Modal fields were not cleared after closing via Close button."

        # --- CYCLE 2: Close via "X" header button ---
        # Step 6: Select Start Date again
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 7: Close modal using the X button in header
        assert page.click_close_x_modal_fiscal_year(), "Failed to click X button on modal header."
        time.sleep(1)
        assert not page.is_fiscal_year_modal_visible(), "Modal was not closed after clicking X button."

        # Step 8 & 9: Reopen modal and verify fields are cleared
        assert page.click_add_fiscal_year_button(), "Failed to reopen '+ Add Fiscal Year' modal."
        assert page.is_fiscal_year_modal_visible(), "Modal failed to display upon reopening."
        assert page.verify_modal_fields_are_cleared(), "Modal fields were not cleared after closing via X button."

        # --- CYCLE 3: Close by clicking outside modal area ---
        # Step 10: Select Start Date again
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 11: Close modal by clicking outside
        assert page.click_outside_modal_fiscal_year(), "Failed to click outside modal area."
        time.sleep(1)
        assert not page.is_fiscal_year_modal_visible(), "Modal was not closed after clicking outside."

        # Step 12 & 13: Reopen modal and verify fields are cleared
        assert page.click_add_fiscal_year_button(), "Failed to reopen '+ Add Fiscal Year' modal."
        assert page.is_fiscal_year_modal_visible(), "Modal failed to display upon reopening."
        assert page.verify_modal_fields_are_cleared(), "Modal fields were not cleared after clicking outside."