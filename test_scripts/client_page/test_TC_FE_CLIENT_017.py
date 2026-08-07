from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_017(client_page):
    """Verify that data in Add Client modal is cleared when closed and reopened."""
    page = client_page


    # --- Pass 1: Close via Cancel Button ---
    # Steps 1–9: Open modal and enter valid data in all fields
    page.click_add_client_button()
    page.fill_client_form()

    # Step 10: Click Cancel/Close button inside modal footer
    page.click_close()

    # Step 11: Reopen modal and verify fields are cleared
    page.click_add_client_button()
    assert page.verify_client_modal_fields_are_empty(), \
        "Modal fields were not cleared after closing via Cancel button and reopening."

    # --- Pass 2: Close via Header 'X' / Close Button ---
    # Step 12: Enter valid data again
    page.fill_client_form()

    # Step 13: Click the Close 'X' button in the modal header
    page.click_close_x()

    # Step 14: Reopen modal and verify fields are cleared
    page.click_add_client_button()
    assert page.verify_client_modal_fields_are_empty(), \
        "Modal fields were not cleared after closing via header 'X' button and reopening."

    # --- Pass 3: Close via Clicking Outside the Modal ---
    # Step 15: Enter valid data again
    page.fill_client_form()

    # Step 16: Click outside the modal to close it
    page.click_outside_modal()

    # Step 17: Reopen modal and verify fields are cleared
    page.click_add_client_button()
    assert page.verify_client_modal_fields_are_empty(), \
        "Modal fields were not cleared after closing via clicking outside modal and reopening."

    