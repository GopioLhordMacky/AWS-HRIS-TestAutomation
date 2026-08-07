from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


def test_tc_fe_clients_046(client_page):
    """Verify Phone Number Field Accepts Valid Phone Number Format in Add Modal."""
    page = client_page

    # Step 1: Open Add Client Modal
    page.click_edit_btn_by_row_index(  row_idx=1)

    # Steps 2–4: Fill client form using the target valid phone number
    page.update_client_form(
        phone="09171234567"
    )

    # Step 5: Click Save button to submit the form
    page.click_save_only()

    # Verification: Ensure no validation error alert/message is triggered
    assert not page.check_error_message(), \
        "Expected valid phone number '09171234567' to be accepted, but validation error appeared."

    