import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_019(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Read row 1 cell values using individual page object getters
        row_fiscal_year = page.get_table_fiscal_year()
        row_fy_code = page.get_table_fy_code()

        # Step 1 & Expected 1: Click edit pencil icon on the target row
        assert page.click_edit_fiscal_year(), "Failed to click edit pencil icon."

        # Step 2 & Expected 2: Verify Update Fiscal Year modal opens
        assert page.is_fiscal_year_modal_visible(), "Update Fiscal Year modal failed to open."

        # Step 3 & Expected 3: Verify modal input values match the selected row's data
        assert page.get_auto_fiscal_year() == row_fiscal_year, (
            f"Modal Fiscal Year value '{page.get_auto_fiscal_year()}' does not match table value '{row_fiscal_year}'."
        )
        assert page.get_auto_fy_code() == row_fy_code, (
            f"Modal FY Code value '{page.get_auto_fy_code()}' does not match table value '{row_fy_code}'."
        )