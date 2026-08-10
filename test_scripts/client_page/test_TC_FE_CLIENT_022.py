from selenium.webdriver import Keys

from locators.client_page_locators import Filter_and_Search_Section
from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_022(self, authenticated_driver):
        """
        (Accessibility) Verify that Industry dropdown can be navigated 
        and activated using keyboard.
        """
        page = go_to_client_page(authenticated_driver, via="url")
        column_name = "Industry"
        target_industry = "Automotive"
        # Step 1: Navigate to the Industry Dropdown via TAB
        # Step 2-4: Send ENTER (open menu) -> ARROW_DOWN (highlight Automotive) -> ENTER (select)

        assert page.tab_navigation_industry_filter(), "Failed to navigate and select Industry dropdown option using keyboard."

        # Step 5: Verify that selected option correctly updates and reflects in the table across all pages
        assert page.check_table_data_by_dropdown_client(column_name, target_industry), f"Expected table to filter for '{target_industry}' via keyboard navigation, but table check failed."

        



        