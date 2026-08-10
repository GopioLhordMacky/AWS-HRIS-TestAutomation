from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:
    def test_tc_fe_clients_021(self, authenticated_driver):
        """Verify that the Industry dropdown selection filters the data displayed in the table."""
        page = go_to_client_page(authenticated_driver, via="url")

        target_dropdown = "Industry"
        target_industry = "Automotive"
        # Step 1: Select "Information Technology Services" from the Industry filter dropdown
        page.select_industry_filter_dropdown_client(target_industry)
        time.sleep(3)

        # Step 2: Verify that all table rows across all pages match the selected industry
        assert page.check_table_data_by_dropdown_client(
            target_dropdown,
            target_industry
        ), f"Expected all table records in 'Industry' column to contain '{target_industry}', but found mismatching records."

