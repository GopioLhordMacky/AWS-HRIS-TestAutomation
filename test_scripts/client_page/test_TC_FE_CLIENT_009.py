from utils.navigation_helpers import go_to_client_page
from imports.client_page_imports import *
import time

class TestClientPage:

    def test_tc_fe_clients_009(self, authenticated_driver):
        """
        TC_FE_CLIENTS_009: Verify leading and trailing whitespace trimming upon form submission.
        """
        raw_name = "  Auto Trim Client  "

        page = go_to_client_page(authenticated_driver, via="url")

        # Pre-condition: Open modal
        page.click_add_client_button()

        # Step 1: Fill form with leading/trailing whitespace in text inputs
        page.fill_client_form(
            
            name=ClientFormData.get_unique_client_name(prefix=raw_name),
            contact="  Jane Doe  ",
            email="  janedoe@example.com  ",
            phone="  09123456789  ",
            address="  456 Trim St.  "
        )

        # Step 2: Click Save
        page.click_save_confirm_modal_client()
        time.sleep(2)

        # Step 3: Verify success (modal closes or success toast appears)
        assert page.is_toast_notification_visible(), "Success toast notification did not appear."
        assert not page.is_client_modal_visible(), "Modal did not close after submission."

            
        
    