import time
from data.fiscal_year_page_inputs import FillStartDate
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_012(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Instantiate dynamic start date (contains input date & all expected calculated fields)
        start_data = FillStartDate()

        # Pre-condition: Open 'Add Fiscal Year' modal
        assert page.click_add_fiscal_year_button(), "Failed to click '+ Add Fiscal Year' button."
        assert page.is_fiscal_year_modal_visible(), "The 'Add Fiscal Year' modal failed to pop up."

        # Step 1: Select a valid Start Date
        assert page.fill_fiscal_year_form(start_data.date_str), f"Failed to input start date '{start_data.date_str}'."
        time.sleep(2)
        # Step 2: Verify that End Date, Fiscal Year, and FY Code fields are automatically populated
        assert page.get_auto_end_date() == start_data.expected_end_date, "End Date was not automatically populated correctly."
        assert page.get_auto_fiscal_year() == start_data.expected_fiscal_year, "Fiscal Year was not automatically populated correctly."
        assert page.get_auto_fy_code() == start_data.expected_fy_code, "FY Code was not automatically populated correctly."

        # Step 3: Click the "Save" button
        assert page.click_save_only_modal_fiscal_year(), "Failed to click Save button."

        assert page.check_toast_message_fiscal_year(expected_text="fiscal year registered successfully"), "Input Start Date failed. Check you Start Date input"
        

        # Step 5: Verify table entry by searching year and validating matched cell outputs
        assert page.verify_saved_fiscal_year_in_table(
            start_date=start_data.date_str,
            end_date=start_data.expected_end_date,
            fiscal_year=start_data.expected_fiscal_year,
            fy_code=start_data.expected_fy_code,
        ), f"Saved record for '{start_data.date_str}' was not found or values mismatched in table."