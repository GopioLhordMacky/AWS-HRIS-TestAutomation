from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_015(self, authenticated_driver):
        """
        Verify Email Address Field Accepts Valid Email Format in Add Modal.
        """
        valid_email ="client@email.com"
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open Add Client Modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."

        # Steps 2–4: Fill client form using the target valid email address
        assert page.fill_client_form(
            
            email=valid_email
        ), "Failed to fill the client form with the valid email address."

        # Step 5: Click Save button to submit the form
        assert page.click_save_only_modal_client(), "Failed to click the Save button on the 'Add Client' modal."

        # Verification: Ensure no validation error alert/message is triggered
        assert not page.check_error_message_client(), f"Expected valid email {valid_email} to be accepted, but validation error appeared."

    