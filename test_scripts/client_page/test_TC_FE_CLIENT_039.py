from utils.navigation_helpers import go_to_client_page
from data.client_page_inputs import ClientFormData
import time

class TestClientPage:
    def test_tc_fe_clients_039(self, authenticated_driver):
        """
        TC_FE_CLIENTS_039: (Functionality) Verify Saving Valid Data in the Update Client Modal

        1. Open "Update Client" modal by clicking the edit icon for a target row.
        2. Fill out client form with new valid data (returns the new client name).
        3. Click save/confirm button to submit updates.
        4. Verify success toast notification appears.
        5. Search for updated Client Name and verify updated data reflects in the table.
        """
        page = go_to_client_page(authenticated_driver, via="url")


        name_update = ClientFormData.get_unique_client_name(prefix="UpdatedClient")
        time.sleep(1)

        # Step 1: Open Update Modal for the target row
        page.click_edit_btn_by_row_index_client()

        # Step 2: Fill form with new valid data and capture generated/updated client name
        page.update_client_form( name=name_update)

        # Step 3: Save changes
        page.click_save_confirm_modal_client()

        # Step 4: Verify toast message confirmation
        assert page.check_toast_message_client(expected_text="Client updated successfully"), \
            "Success toast message was not displayed or did not match expected text."
        
        time.sleep(1.5)  # Allow time for toast message to appear

        # Step 5: Verify updated record reflects in the table via search helper
        assert page.check_table_data_by_search_client(  column_name="Client Name", text=name_update), \
            f"Updated client name '{name_update}' was not found in the table after saving."

        