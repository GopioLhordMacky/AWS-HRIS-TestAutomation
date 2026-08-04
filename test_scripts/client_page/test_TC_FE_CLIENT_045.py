from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_045():
    """Verify Email Address Field Accepts Valid Email Format in Add Modal."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open Add Client Modal
    click_edit_btn_by_row_index(driver, row_idx=1)

    # Steps 2–4: Fill client form using the target valid email address
    update_client_form(
        driver,
        email="client@email.com"
    )

    # Step 5: Click Save button to submit the form
    click_save_only(driver)

    # Verification: Ensure no validation error alert/message is triggered
    assert not check_error_message(driver), \
        "Expected valid email 'client@email.com' to be accepted, but validation error appeared."

    close_browser(driver)