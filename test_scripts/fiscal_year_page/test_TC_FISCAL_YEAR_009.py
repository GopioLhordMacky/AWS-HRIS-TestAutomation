import time
from data.fiscal_year_page_inputs import FillStartDate
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_009(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Instantiate dynamic start date (contains date_str & calculated expectations)
        start_data = FillStartDate()

        # Step 1: Click '+ Add Fiscal Year' button
        assert page.click_add_fiscal_year_button(), "Failed to click '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 2: Select/Fill a valid Start Month
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 3: Observe and verify that End Date, Fiscal Year, and FY Code fields are automatically populated correctly
        assert page.get_auto_end_date() == start_data.expected_end_date, f"Expected End Date '{start_data.expected_end_date}', but got '{page.get_auto_end_date()}'"
        assert page.get_auto_fiscal_year() == start_data.expected_fiscal_year, f"Expected Fiscal Year '{start_data.expected_fiscal_year}', but got '{page.get_auto_fiscal_year()}'"
        assert page.get_auto_fy_code() == start_data.expected_fy_code, f"Expected FY Code '{start_data.expected_fy_code}', but got '{page.get_auto_fy_code()}'"