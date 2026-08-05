from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.ongoing
def test_tc_fe_clients_064(authenticated_driver):
    """
    TC_FE_CLIENTS_064: (Functionality) Verify Input Fields Accept a Maximum of 255 Characters Only
    
    1. Click 'Add Client' button to open the modal.
    2. Fill form using fill_client_form with a 256-character string in the name field.
    3. Click save_only.
    4. Verify that an error message is observed using check_error_message.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open Add Client Modal
    click_add_client_button(driver, timeout=10)
    time.sleep(1)

    # Prepare string exceeding 255 characters (256 chars)
    invalid_256_char_string = "A" * 230
    client_name = ClientFormData.get_unique_client_name(prefix = invalid_256_char_string)  # Generate a unique client name for testing

    # Step 2: Fill client form with 256-character string
    fill_client_form(
        driver,
        name=client_name,
        industry=ClientFormData.VALID_INDUSTRY,
        country=ClientFormData.VALID_COUNTRY,
        contact=ClientFormData.VALID_CONTACT_PERSON,
        email=ClientFormData.VALID_EMAIL,
        phone=ClientFormData.VALID_PHONE,
        address=ClientFormData.VALID_ADDRESS
    )

    # Step 3: Trigger form save
    click_save_confirm (driver)
    time.sleep(1)

    # Step 1: Open Add Client Modal
    click_add_client_button(driver, timeout=10)
    time.sleep(1)

    # Prepare string exceeding 255 characters (256 chars)
    invalid_256_char_string = "A" * 256
    client_name = ClientFormData.get_unique_client_name(prefix = invalid_256_char_string)  # Generate a unique client name for testing

    # Step 2: Fill client form with 256-character string
    fill_client_form(
        driver,
        name=client_name,
        industry=ClientFormData.VALID_INDUSTRY,
        country=ClientFormData.VALID_COUNTRY,
        contact=ClientFormData.VALID_CONTACT_PERSON,
        email=ClientFormData.VALID_EMAIL,
        phone=ClientFormData.VALID_PHONE,
        address=ClientFormData.VALID_ADDRESS
    )

    # Step 3: Trigger form save
    click_save_only(driver)
    time.sleep(1)

    # Step 4: Verify validation error message appears
    assert check_error_message(driver, timeout=5), (
        "Expected validation error message after submitting input exceeding 255 characters, but none was observed!"
    )

    close_browser(driver)