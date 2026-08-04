from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_039():
    """
    TC_FE_CLIENTS_039: (Functionality) Verify Saving Valid Data in the Update Client Modal
    
    1. Open "Update Client" modal by clicking the edit icon for a target row.
    2. Fill out client form with new valid data (returns the new client name).
    3. Click save/confirm button to submit updates.
    4. Verify success toast notification appears.
    5. Search for updated Client Name and verify updated data reflects in the table.
    """
    driver = open_browser("chrome")
    login_client_page(driver)
    name_update = ClientFormData.get_unique_client_name(prefix="UpdatedClient")
    target_row_idx = 1
    time.sleep(2)

    # Step 1: Open Update Modal for the target row
    click_edit_btn_by_row_index(driver, row_idx=target_row_idx)

    # Step 2: Fill form with new valid data and capture generated/updated client name
    update_client_form(driver, name=name_update)

    # Step 3: Save changes
    click_save_confirm(driver)

    # Step 4: Verify toast message confirmation
    assert check_toast_message(driver, expected_text="Client updated successfully"), \
        "Success toast message was not displayed or did not match expected text."
    
    time.sleep(1.5)  # Allow time for toast message to appear
    driver.refresh()

    # Step 5: Verify updated record reflects in the table via search helper
    assert check_table_data_by_search(driver, column_name="Client Name", text=name_update), \
        f"Updated client name '{name_update}' was not found in the table after saving."

    close_browser(driver)