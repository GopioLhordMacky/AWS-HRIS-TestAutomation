from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage: 

    def test_tc_fe_clients_055(self, authenticated_driver):
        """
        TC_FE_CLIENTS_055: (Functionality) Verify the Toggling Updates the Correct Client Record
        
        1. Filter by Status: Inactive using React-Select dropdown.
        2. Record initial pagination info using helper function.
        3. Toggle the active status for row 1 and click Confirm in the modal.
        4. Record updated pagination info using helper function.
        5. Assert that initial and updated pagination info are not equal.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Filter dropdown by "Inactive" status
        page.select_status_filter_client("Inactive")
        time.sleep(2)

        # Step 2: Capture initial pagination count text via helper
        initial_pagination_info = page.get_pagination_information_client()

        # Step 3: Toggle status on row 1
        page.toggle_active_status_client(row_index=1, column_name="Active")
        
        # Confirm the status change in modal dialog
        page.click_confirm_modal_client ()
        time.sleep(2)

        # Step 4: Capture updated pagination count text via helper
        updated_pagination_info = page.get_pagination_information_client()

        # Step 5: Assertion
        assert initial_pagination_info != updated_pagination_info, (
            f"Pagination count did not update after toggling record status! "
            f"Initial: '{initial_pagination_info}' | Updated: '{updated_pagination_info}'"
        )

