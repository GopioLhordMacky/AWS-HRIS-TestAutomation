from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_054(authenticated_driver):
    """
    TC_FE_CLIENTS_054: (Functionality) Verify Toggle Button with Confirmation Message
    
    1. Click the toggle switch on a target row to initiate a status change.
    2. Verify that the confirmation dialog/message appears immediately.
    3. Verify that both 'Confirm' and 'Cancel' options are visible to the user.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    target_row = 1
    target_col = "Active"

    # Step 1: Click the toggle switch
    FormControls.toggle_active_status(driver, row_index=target_row, column_name=target_col)
    # FormControls.toggle_active_status(driver, row_index=target_row, column_name=target_col)

    # Step 2 & 3: Check visibility of the confirmation controls
    assert ComponentVerifier.is_component_visible(driver, ModalLocators.CONFIRM_BUTTON), \
        "Confirmation dialog's CONFIRM button is not visible!"
        
    assert ComponentVerifier.is_component_visible(driver, ModalLocators.CANCEL_BUTTON), \
        "Confirmation dialog's CANCEL button is not visible!"

    # Clean up modal view if needed (optional)
    ElementActions.wait_for_and_click(driver, *ModalLocators.CANCEL_BUTTON)

