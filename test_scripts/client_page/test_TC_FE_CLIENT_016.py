
from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_016(self, authenticated_driver):
        """
        Verify Phone Number Field Accepts Valid Phone Number Format in Add Modal.
        """
        page = go_to_client_page(authenticated_driver, via="url")
        valid_phone_number = "09171234567"
        
        # Step 1: Open Add Client Modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button." 

        # Steps 2–4: Fill client form using the target valid phone number
        page.fill_client_form(
            
            phone=valid_phone_number
        )

        # Step 5: Click Save button to submit the form
        page.click_save_only_modal_client()

        # Verification: Ensure no validation error alert/message is triggered
        assert not page.check_error_message_client(), f"Expected valid phone number '{valid_phone_number}' to be accepted, but validation error appeared."

    