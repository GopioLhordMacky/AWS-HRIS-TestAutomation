from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_012(driver):
    """Verify system prevents duplicate client creation in Add Client Modal."""
    login_client_page(driver)

    # # Pre-condition: Create an initial client to trigger duplicate scenario
    existing_name = ClientFormData.get_unique_client_name(prefix="DuplicateName")
    click_add_client_button(driver)
    fill_client_form(driver, name=existing_name)
    ModalActions.click_save_confirm(driver)
    time.sleep(3)
    # Step 1: Open modal to attempt duplicate creation
    click_add_client_button(driver)

    # Step 2: Fill form matching the existing client record
    fill_client_form(driver, name=existing_name)

    # Step 3: Click Save
    ModalActions.click_save_only(driver)

    # Assertions
    assert ComponentVerifier.check_error_message(driver, expected_text="Client already exists"), \
        "Expected 'Client already exists' error message was not displayed."

    driver.quit()