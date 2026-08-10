from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:
    def test_tc_fe_clients_039(self, authenticated_driver):
        """
        TC_FE_CLIENTS_039: (Functionality) Verify Error Message When Saving Duplicate Client Name in the Update Client Modal
        
        1. Open "Update Client" modal by clicking the edit icon for a target row.
        2. Fill out client form with a duplicate client name (returns the duplicate name).
        3. Click save/confirm button to submit updates.
        4. Verify error message appears indicating duplicate client name.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        name_update = "Duplicate Test Automation"
        time.sleep(1)

        # Step 1: Open Update Modal for the target row
        page.click_edit_btn_by_row_index_client()

        # Step 2: Fill form with new valid data and capture generated/updated client name
        page.update_client_form(name=name_update)

        # Step 3: Save changes
        page.click_save_only_modal_client()

        # Step 4: Verify error message confirmation
        assert page.check_error_message_client(expected_text="Cannot update: A client with this name already exists")," Error message was not displayed or did not match expected text."
