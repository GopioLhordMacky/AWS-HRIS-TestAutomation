from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_018():
    """Verify 'Add Client' Modal Closes When Clicking Outside of the Modal."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open the "Add Client" modal
    click_add_client_button(driver)

    # Fill out the form to test that entered data is not persisted
    fill_client_form(driver)

    # Step 2: Click outside the modal to close it
    click_outside_modal(driver)

    # Verification: Reopen the modal and verify all fields are cleared (data was not saved)
    click_add_client_button(driver)
    assert verify_client_modal_fields_are_empty(driver), \
        "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    close_browser(driver)