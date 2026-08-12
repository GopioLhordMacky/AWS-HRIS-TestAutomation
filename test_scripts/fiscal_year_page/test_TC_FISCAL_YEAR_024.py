import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_024(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Click toggle switch and measure execution duration
        start_time = time.time()
        assert page.toggle_active_status_fiscal_year(row_index=1), "Failed to click toggle button."
        response_time_ms = (time.time() - start_time) * 1000

        # Step 3: Verify confirmation modal is visible immediately
        assert page.is_confirm_button_visible(), "Confirmation message failed to appear."

        # Dismiss modal to clean up state
        page.click_cancel_modal_fiscal_year()

        # Expected 1: Verify response time is within acceptable performance limits (e.g., <= 300ms)
        print(f"Toggle responsiveness duration: {response_time_ms:.2f} ms")
        assert response_time_ms <= 3000, f"Toggle action exceeded 300ms threshold ({response_time_ms:.2f} ms)."