from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_008(self, authenticated_driver):
        """TC_FE_CLIENTS_008: Verify validation when text input fields contain only whitespace."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open Add Client Modal
        page.click_add_client_button()

        # Step 2: Fill text fields with whitespace and valid dropdowns
        page.fill_client_form(
            contact="   ",
            email="   ",
            phone="   ",
            address="   "
        )

        # Step 3: Click Save
        assert page.click_save_only_modal_client(), "Failed to click Save button on the 'Add Client' modal."

        # Step 4: Verify validation message triggers & modal stays open
        assert page.check_error_message_client("Required!"), "Validation message for 'Client Name' not displayed."

        assert page.is_client_modal_visible(), "Modal closed unexpectedly."
