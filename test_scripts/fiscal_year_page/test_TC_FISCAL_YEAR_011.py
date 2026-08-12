import time
from data.fiscal_year_page_inputs import FillStartDate
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_011(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Instantiate dynamic start date (contains date_str, expected_fiscal_year & expected_fy_code)
        start_data = FillStartDate()

        # Pre-condition: Click '+ Add Fiscal Year' button to open modal
        assert page.click_add_fiscal_year_button(), "Failed to click '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 1 & 2: Select/Fill a valid Start Date
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."

        # Step 3 & 4: Observe and compare the displayed Fiscal Year and FY Code with expected calculated values
        actual_fiscal_year = page.get_auto_fiscal_year()
        actual_fy_code = page.get_auto_fy_code()

        assert actual_fiscal_year == start_data.expected_fiscal_year, (
            f"Expected Fiscal Year '{start_data.expected_fiscal_year}', but got '{actual_fiscal_year}'"
        )
        assert actual_fy_code == start_data.expected_fy_code, (
            f"Expected FY Code '{start_data.expected_fy_code}', but got '{actual_fy_code}'"
        )