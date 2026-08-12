import time
from data.fiscal_year_page_inputs import FillStartDate
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_010(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Instantiate dynamic start date (contains date_str & expected_end_date)
        start_data = FillStartDate()

        # Step 1: Open 'Add Fiscal Year' modal
        assert page.click_add_fiscal_year_button(), "Failed to click '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 2: Select/Fill a valid Start Date
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 3, 4 & 5: Observe and compare the displayed End Date with the expected 12-month period End Date
        actual_end_date = page.get_auto_end_date()
        assert actual_end_date == start_data.expected_end_date, (
            f"Expected 12-month End Date '{start_data.expected_end_date}', but got '{actual_end_date}'"
        )