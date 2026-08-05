from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_039(authenticated_driver):
    """
    TC_FE_CLIENTS_039: (Functionality) Verify Saving Valid Data in the Update Client Modal
    
    1. Open "Update Client" modal by clicking the edit icon for a target row.
    2. Fill out client form with new valid data (returns the new client name).
    3. Click save/confirm button to submit updates.
    4. Verify success toast notification appears.
    5. Search for updated Client Name and verify updated data reflects in the table.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    name_update = ClientFormData.get_unique_client_name(prefix="UpdatedClient")
    target_row_idx = 1
    time.sleep(2)

    # Step 1: Open Update Modal for the target row
    TableActions.click_edit_btn_by_row_index(driver, row_idx=target_row_idx)

    # Step 2: Fill form with new valid data and capture generated/updated client name
    ClientPage.update_client_form(driver, name=name_update)

    # Step 3: Save changes
    ModalActions.click_save_confirm(driver)

    # Step 4: Verify toast message confirmation
    assert ModalNotifications.check_toast_message(driver, expected_text="Client updated successfully"), \
        "Success toast message was not displayed or did not match expected text."
    
    time.sleep(1.5)  # Allow time for toast message to appear
    driver.refresh()

    # Step 5: Verify updated record reflects in the table via search helper
    assert TableSearch.check_table_data_by_search(driver, column_name="Client Name", text=name_update), \
        f"Updated client name '{name_update}' was not found in the table after saving."

    driver.quit()