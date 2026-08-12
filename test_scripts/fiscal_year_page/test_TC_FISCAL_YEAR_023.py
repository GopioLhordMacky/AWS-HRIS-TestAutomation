import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_023(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Filter table by 'Inactive' status
        assert page.select_status_filter_fiscal_year("Inactive"), "Failed to filter table by 'Inactive'."
        time.sleep(1)

        # Record initial pagination info before toggle (e.g., '1-10 of 25')
        initial_pagination = page.get_pagination_information_client()

        # Step 2-4: Click toggle on row 1, verify confirmation modal, and confirm
        assert page.toggle_active_status_fiscal_year(row_index=1), "Failed to click toggle switch."
        assert page.click_confirm_modal_fiscal_year(), "Failed to click Confirm in modal."

        time.sleep(1)

        # Step 5: Refresh page to check persistence
        authenticated_driver.refresh()
        time.sleep(1)

        # Ensure filter is still on 'Inactive' after refresh
        page.select_status_filter_fiscal_year("Inactive")
        time.sleep(1)

        # Step 6: Capture new pagination info and verify it has changed (-1 record in 'Inactive')
        toggled_pagination = page.get_pagination_information_fiscal_year()
        assert initial_pagination != toggled_pagination, (
            f"Pagination info did not change after refresh. Initial: '{initial_pagination}', Current: '{toggled_pagination}'."
        )