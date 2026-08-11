from utils.navigation_helpers import go_to_client_page
from data.client_page_inputs import ClientFormData
import time

class TestClientPage:

    def test_tc_fe_clients_064(self, authenticated_driver):
        """
        TC_FE_CLIENTS_064: (Functionality) Verify Input Fields Accept a Maximum of 255 Characters Only
        
        1. Click 'Add Client' button to open the modal.
        2. Fill form using fill_client_form with a 256-character string in the name field.
        3. Click save_only.
        4. Verify that an error message is observed using check_error_message.
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # # Step 1: Open Add Client Modal
        # page.click_add_client_button(  )
        # time.sleep(1)

        # # Prepare string exceeding 255 characters (256 chars)
        # invalid_256_char_string = "A" * 230
        # client_name = ClientFormData.get_unique_client_name(prefix = invalid_256_char_string)  # Generate a unique client name for testing

        # # Step 2: Fill client form with 256-character string
        # page.fill_client_form(
            
        #     name=client_name,
        #     industry=ClientFormData.VALID_INDUSTRY,
        #     country=ClientFormData.VALID_COUNTRY,
        #     contact=ClientFormData.VALID_CONTACT_PERSON,
        #     email=ClientFormData.VALID_EMAIL,
        #     phone=ClientFormData.VALID_PHONE,
        #     address=ClientFormData.VALID_ADDRESS
        # )

        # # Step 3: Trigger form save
        # page.click_save_confirm_modal_client()
        # time.sleep(1)

        # Step 1: Open Add Client Modal
        page.click_add_client_button(  )
        time.sleep(1)

        # Prepare string exceeding 255 characters (256 chars)
        # invalid_256_char_string = "A" * 256
        # client_name = ClientFormData.get_unique_client_name(prefix = invalid_256_char_string)  # Generate a unique client name for testing

        # Step 2: Fill client form with 256-character string
        page.fill_client_form(
            name=ClientFormData.LONG_CLIENT_NAME,
        )
        time.sleep(1)
        # Step 3: Trigger form save
        page.click_save_only_modal_client()
        time.sleep(1)

        # Step 4: Verify validation error message appears
        assert page.check_error_message_client(expected_text="Client Name exceeded the 255 maximum character limit!"), (
            "Expected validation error message after submitting input exceeding 255 characters, but none was observed!"
        )

