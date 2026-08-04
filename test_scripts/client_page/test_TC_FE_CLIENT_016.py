from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_016():
    """Verify Phone Number Field Accepts Valid Phone Number Format in Add Modal."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open Add Client Modal
    click_add_client_button(driver)

    # Steps 2–4: Fill client form using the target valid phone number
    fill_client_form(
        driver,
        phone="09171234567"
    )

    # Step 5: Click Save button to submit the form
    click_save_only(driver)

    # Verification: Ensure no validation error alert/message is triggered
    assert not check_error_message(driver), \
        "Expected valid phone number '09171234567' to be accepted, but validation error appeared."

    close_browser(driver)