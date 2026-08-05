from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page
@pytest.mark.passed
def test_tc_fe_clients_046(authenticated_driver):
    """Verify Phone Number Field Accepts Valid Phone Number Format in Add Modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open Add Client Modal
    click_edit_btn_by_row_index(driver, row_idx=1)

    # Steps 2–4: Fill client form using the target valid phone number
    update_client_form(
        driver,
        phone="09171234567"
    )

    # Step 5: Click Save button to submit the form
    click_save_only(driver)

    # Verification: Ensure no validation error alert/message is triggered
    assert not check_error_message(driver), \
        "Expected valid phone number '09171234567' to be accepted, but validation error appeared."

    close_browser(driver)