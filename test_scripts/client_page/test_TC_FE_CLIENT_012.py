from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_012(client_page):
    """Verify system prevents duplicate client creation in Add Client Modal."""
    page = client_page


    # # Pre-condition: Create an initial client to trigger duplicate scenario
    existing_name = ClientFormData.get_unique_client_name(prefix="DuplicateName")
    page.click_add_client_button()
    page.fill_client_form(  name=existing_name)
    page.click_save_confirm()
    time.sleep(3)
    # Step 1: Open modal to attempt duplicate creation
    page.click_add_client_button()

    # Step 2: Fill form matching the existing client record
    page.fill_client_form(  name=existing_name)

    # Step 3: Click Save
    page.click_save_only()

    # Assertions
    assert page.check_error_message( expected_text="Client already exists"), \
        "Expected 'Client already exists' error message was not displayed."

    