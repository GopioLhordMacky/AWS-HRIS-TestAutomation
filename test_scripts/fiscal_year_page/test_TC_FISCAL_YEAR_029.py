import time
from utils.navigation_helpers import go_to_fiscal_year_page
from selenium.webdriver.common.by import By


class TestFiscalYearPage:

    def test_tc_fe_fiscal_year_029(self, authenticated_driver):
        page = go_to_fiscal_year_page(authenticated_driver, via="url")


        expected_counts = [10, 20, 50, 100]

        # Step 2: Iterate through options and verify table updates dynamically
        for count in expected_counts:
            page.change_rows_per_page_fiscal_year(count)
            time.sleep(1.5)

            # Get updated pagination text and visible row count
            updated_pag_info = page.get_pagination_information_fiscal_year()
            visible_rows = len(page.find_elements_len(By.XPATH, "//tbody/tr"))

            # Assertions
            assert visible_rows <= count, (
                f"Displayed table rows ({visible_rows}) exceed selected limit ({count})!"
            )
            assert updated_pag_info is not None and len(updated_pag_info) > 0, (
                f"Pagination info is empty after setting rows per page to {count}!"
            )

