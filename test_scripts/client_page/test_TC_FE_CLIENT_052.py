from utils.navigation_helpers import go_to_client_page
from selenium.webdriver.common.by import By
import time

class TestClientPage:

    def test_tc_fe_clients_052(self, authenticated_driver):
        """
        TC_FE_CLIENTS_052: (Functionality) Verify Active toggle default state for Active records
        
        1. Navigate to Clients page.
        2. Filter records by Status: Active (if filter dropdown is present).
        3. Iterate through rows in the table and verify Active toggle state is ON (True).
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Optional: If you have a status filter helper to ensure only Active records are shown
        # filter_by_status(  status="Active")

        target_column = "Active"
        page.change_rows_per_page_client(100)  
        time.sleep(2)  
        # Get total visible rows on current view\
        col_idx = page.get_column_index_client(target_column)
        row_count = len(page.find_elements_len(By.XPATH, f"//body/tr/td[{col_idx}]"))

        for row_idx in range(1, row_count + 1):
            is_active = page.verify_active_toggle_state_client(column_name=target_column)
            assert is_active, f"Expected Active toggle to be ACTIVE for row {row_idx}, but found INACTIVE"


