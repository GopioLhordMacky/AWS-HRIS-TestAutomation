import time
from data.client_page_inputs import ClientFormData
from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_012(self, authenticated_driver):
        """Verify system prevents duplicate client creation in Add Client Modal."""
        page = go_to_client_page(authenticated_driver, via="url")

        # # Pre-condition: Create an initial client to trigger duplicate scenario
        existing_name = ClientFormData.get_unique_client_name(prefix="DuplicateName")
        page.click_add_client_button()
        page.fill_client_form(name=existing_name)
        page.click_save_confirm_modal_client()
        time.sleep(3)
        
        # Step 1: Open modal to attempt duplicate creation
        page.click_add_client_button()

        # Step 2: Fill form matching the existing client record
        page.fill_client_form(name=existing_name)

        # Step 3: Click Save
        page.click_save_only_modal_client()

        # Assertions
        assert page.check_error_message_client(expected_text="Client already exists"), \
            "Expected 'Client already exists' error message was not displayed."

    