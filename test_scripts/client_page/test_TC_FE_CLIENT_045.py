from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_045(self, authenticated_driver):
        """Verify Email Address Field Accepts Valid Email Format in Add Modal."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open Add Client Modal
        assert page.click_edit_btn_by_row_index_client(), "Failed to click Edit button"

        # Steps 2–4: Fill client form using the target valid email address
        page.update_client_form(
            email="client@email.com"
        )

        # Step 5: Click Save button to submit the form
        assert page.click_save_only_modal_client(), "Failed to click Save button"

        # Verification: Ensure no validation error alert/message is triggered
        assert not page.check_error_message_client(), \
            "Expected valid email 'client@email.com' to be accepted, but validation error appeared."

        