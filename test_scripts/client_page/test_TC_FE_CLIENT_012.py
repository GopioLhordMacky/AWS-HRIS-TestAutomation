from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_012(authenticated_driver):
    """Verify system prevents duplicate client creation in Add Client Modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # # Pre-condition: Create an initial client to trigger duplicate scenario
    existing_name = ClientFormData.get_unique_client_name(prefix="DuplicateName")
    ClientPage.click_add_client_button(driver)
    ClientPage.fill_client_form(driver, name=existing_name)
    ModalActions.click_save_confirm(driver)
    time.sleep(3)
    # Step 1: Open modal to attempt duplicate creation
    ClientPage.click_add_client_button(driver)

    # Step 2: Fill form matching the existing client record
    ClientPage.fill_client_form(driver, name=existing_name)

    # Step 3: Click Save
    ModalActions.click_save_only(driver)

    # Assertions
    assert ModalNotifications.check_error_message(driver, expected_text="Client already exists"), \
        "Expected 'Client already exists' error message was not displayed."

    driver.quit()