from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


def test_tc_fe_clients_008(client_page):
    """TC_FE_CLIENTS_008: Verify validation when text input fields contain only whitespace."""
    page = client_page

    # Step 1: Open Add Client Modal
    page.click_add_client_button()

    # Step 2: Fill text fields with whitespace and valid dropdowns
    page.fill_client_form(
         
        contact="   ",
        email="   ",
        phone="   ",
        address="   "
    )

    # Step 3: Click Save
    page.click_save_only()

    # Step 4: Verify validation message triggers & modal stays open
    assert page.is_component_visible(
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message failed to appear for whitespace-only input."

    assert page.is_component_visible(Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly."
