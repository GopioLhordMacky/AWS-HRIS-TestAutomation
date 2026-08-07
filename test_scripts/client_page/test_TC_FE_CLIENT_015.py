from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_015(client_page):
    """Verify Email Address Field Accepts Valid Email Format in Add Modal."""
    page = client_page


    # Step 1: Open Add Client Modal
    page.click_add_client_button()

    # Steps 2–4: Fill client form using the target valid email address
    page.fill_client_form(
         
        email="client@email.com"
    )

    # Step 5: Click Save button to submit the form
    page.click_save_only()

    # Verification: Ensure no validation error alert/message is triggered
    assert not page.check_error_message(), \
        "Expected valid email 'client@email.com' to be accepted, but validation error appeared."

    