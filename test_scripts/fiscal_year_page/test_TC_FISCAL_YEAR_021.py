import time
from utils.navigation_helpers import go_to_fiscal_year_page


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_021(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")

        # Step 1 & 2: Verify Ascending sort on "Fiscal Year" column
        assert page.verify_column_sorting_fiscal_year(column_name="Fiscal Year", order="ascending"), (
            "Fiscal Year column was not sorted correctly in ascending order."
        )

        # Step 1 & 2: Verify Descending sort on "Fiscal Year" column
        assert page.verify_column_sorting_fiscal_year(column_name="Fiscal Year", order="descending"), (
            "Fiscal Year column was not sorted correctly in descending order."
        )