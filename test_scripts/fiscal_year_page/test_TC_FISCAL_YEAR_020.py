import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_019(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1-3 & Expected 1-3: Verify first row data matches opened edit modal fields
        assert page.verify_table_row_data_matches_edit_modal(), (
            "Data displayed in Update Fiscal Year modal does not match the selected table record."
        )