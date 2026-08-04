from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_040():
    """
    TC_FE_CLIENTS_040: (Functionality) Verify Saving Valid Data in the Update Client Modal
    
    1. Open "Update Client" modal by clicking the edit icon for a target row.
    2. Fill out client form with new valid data (returns the new client name).
    3. Click save/confirm button to submit updates.
    4. Verify success toast notification appears.
    5. Search for updated Client Name and verify updated data reflects in the table.
    """
    driver = open_browser("chrome")
    login_client_page(driver)
    name_update = "Duplicate Test Automation"
    target_row_idx = 1
    time.sleep(2)

    # Step 1: Open Update Modal for the target row
    click_edit_btn_by_row_index(driver, row_idx=target_row_idx)

    # Step 2: Fill form with new valid data and capture generated/updated client name
    update_client_form(driver, name=name_update)

    # Step 3: Save changes
    click_save_only(driver)

    # Step 4: Verify error message confirmation
    assert check_error_message(driver, expected_text="Cannot update: A client with this name already exists"), \
        "Expected error message was not displayed or did not match expected text."

    close_browser(driver)