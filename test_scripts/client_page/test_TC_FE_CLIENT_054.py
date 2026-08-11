from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_054(self, authenticated_driver):
        """
        TC_FE_CLIENTS_054: (Functionality) Verify Toggle Button with Confirmation Message
        
        1. Click the toggle switch on a target row to initiate a status change.
        2. Verify that the confirmation dialog/message appears immediately.
        3. Verify that both 'Confirm' and 'Cancel' options are visible to the user.
        """
        page = go_to_client_page(authenticated_driver, via="url")
        target_row = 1
        target_col = "Active"

        # Step 1: Click the toggle switch
        page.toggle_active_status_client(row_index=target_row, column_name=target_col)

        # Step 2 & 3: Check visibility of the confirmation controls
        assert page.is_confirm_button_visible(), "Confirmation dialog's CONFIRM button is not visible!"
            
        assert page.is_cancel_button_visible(),"Confirmation dialog's CANCEL button is not visible!"

        # Clean up modal view if needed (optional)
        assert page.click_cancel_modal_client(), "Failed to click cancel button"

