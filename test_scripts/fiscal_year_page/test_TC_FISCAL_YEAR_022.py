import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_022(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # --- FLOW 1: CANCEL ACTION ---
        # Step 1-3: Click toggle switch on row 1 to trigger confirmation dialog
        assert page.toggle_active_status_fiscal_year(row_index=1), "Failed to click status toggle switch."

        # Step 4-6 & Expected 1-3: Verify confirmation dialog, text, and buttons (Confirm/Cancel) appear
        assert page.is_confirm_button_visible(), "Confirm button is not visible in the confirmation dialog."
        assert page.is_cancel_button_visible(), "Cancel button is not visible in the confirmation dialog."

        # Expected 5: Click Cancel and verify state remains unchanged
        assert page.click_cancel_modal_fiscal_year(), "Failed to click Cancel button on dialog."
        
        time.sleep(1)

        # --- FLOW 2: CONFIRM ACTION ---
        # Step 1-3: Click toggle switch again to change status
        assert page.select_status_filter_fiscal_year("Inactive"), "Failed to filter Status"

        assert page.toggle_active_status_fiscal_year(row_index=1), "Failed to click status toggle switch."
        # Expected 4: Click Confirm and verify toggle state changes
        assert page.click_confirm_modal_fiscal_year(), "Failed to click Confirm button on dialog."
        assert page.check_toast_message_fiscal_year("The fiscal year is set to active"), (
            "Expected toast message for status update was not displayed."
        )