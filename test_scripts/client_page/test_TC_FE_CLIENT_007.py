from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_007(self, authenticated_driver):
        """TC_FE_CLIENTS_007: Verify required input validation on empty form submission."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Pre-condition: Open Add Client Modal
        page.click_add_client_button()

        assert page.is_client_modal_visible(), "The 'Add Client' modal failed to pop up."
        
        # Step 1: Click Save with all required fields left blank
        assert page.click_save_only_modal_client(), "Failed to click Save button on the 'Add Client' modal."
        
        # Step 2: Verify validation message pops up
        assert page.is_toast_notification_visible(), "Validation message 'Client Name is required!' failed to display."
        
        # Step 3: Verify modal remains open and does not save/close
        assert page.is_client_modal_visible(), "Modal closed unexpectedly after invalid submission."
        
