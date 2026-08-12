import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_028(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1: Check Previous button state on First Page
        prev_btn = page.find_prev_button()
        assert not prev_btn.is_enabled() or prev_btn.get_attribute("disabled") is not None, \
            "Previous page button should be disabled on the first page!"

        # Step 2: Navigate to Last Page by observing text updates
        while True:
            current_info = page.get_pagination_information_fiscal_year()
            try:
                page.go_to_next_page_fiscal_year()
                time.sleep(1.5)
            except Exception:
                # If wait_for_and_click fails because the button became unclickable/disabled, we've hit the end
                break

            updated_info = page.get_pagination_information_fiscal_year()

            # If pagination range text didn't change after clicking, we are on the last page
            if current_info == updated_info:
                break

        # Step 3: Check Next button state on Last Page
        next_btn = page.find_next_button()
        assert not next_btn.is_enabled() or next_btn.get_attribute("disabled") is not None, \
            "Next page button should be disabled on the last page!"

