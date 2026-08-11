from utils.navigation_helpers import go_to_client_page
import time
# @pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")

class TestClientPage:

    def test_tc_fe_clients_053(self, authenticated_driver):
        """
        TC_FE_CLIENTS_053: (Functionality) Verify Active toggle default state for Active records
        
        1. Navigate to Clients page.
        2. Filter records by Status: Active (if filter dropdown is present).
        3. Iterate through rows in the table and verify Active toggle state is ON (True).
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # Optional: If you have a status filter helper to ensure only Active records are shown
        page.select_status_filter_client("Active")
        time.sleep(2)

        target_column = "Active"
        
        # Step 1 & 2: Check each row to confirm the toggle state is active/ON
        assert page.check_toggle_status_on_table_client(
            column_name="Active",
            text="Inactive"
        ), f"Table failed to filter and display only '{target_column}' records."

