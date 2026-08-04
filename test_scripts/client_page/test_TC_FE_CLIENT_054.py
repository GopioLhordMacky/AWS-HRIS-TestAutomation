from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_054():
    """
    TC_FE_CLIENTS_054: (Functionality) Verify Toggle Button with Confirmation Message
    
    1. Click the toggle switch on a target row to initiate a status change.
    2. Verify that the confirmation dialog/message appears immediately.
    3. Verify that both 'Confirm' and 'Cancel' options are visible to the user.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    target_row = 1
    target_col = "Active"

    # Step 1: Click the toggle switch
    toggle_active_status(driver, row_index=target_row, column_name=target_col)

    # Step 2 & 3: Check visibility of the confirmation controls
    assert is_component_visible(driver, ModalLocators.CONFIRM_BUTTON), \
        "Confirmation dialog's CONFIRM button is not visible!"
        
    assert is_component_visible(driver, ModalLocators.CANCEL_BUTTON), \
        "Confirmation dialog's CANCEL button is not visible!"

    # Clean up modal view if needed (optional)
    wait_for_and_click(driver, *ModalLocators.CANCEL_BUTTON)

    close_browser(driver)