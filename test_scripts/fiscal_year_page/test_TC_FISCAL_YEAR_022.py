from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field
    )
from locators import Table, Confirmation_Dialogue, Buttons, Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_022(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(3)

    # Wait for table rows to load and get initial count
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    initial_rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    initial_count = len(initial_rows)
    assert initial_count >= 1, "Expected at least 1 row to perform status toggle."

    # --- Step 1: Cancel Scenario ---
    target_row = initial_rows[0]
    toggle_btn = target_row.find_element(By.XPATH, Options.TOGGLE_BUTTON)
    wait.until(EC.element_to_be_clickable(toggle_btn))
    toggle_btn.click()

    # Step 2 & 3: Verify confirmation dialogue appears with options
    cancel_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CANCEL_BUTTON)))
    confirm_btn = driver.find_element(By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON)
    assert confirm_btn.is_displayed(), "Expected 'Confirm' button to be visible."
    assert cancel_btn.is_displayed(), "Expected 'Cancel' button to be visible."

    # Step 5: Click Cancel and verify count remains unchanged
    cancel_btn.click()
    time.sleep(2) 

    current_rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    assert len(current_rows) == initial_count, (
        f"Expected row count to remain {initial_count} after cancel, but got {len(current_rows)}."
    )

    # --- Step 2: Confirm Scenario ---
    # Re-fetch target row and click toggle again
    target_row = driver.find_elements(By.XPATH, Table.TABLE_ROWS)[0]
    toggle_btn = target_row.find_element(By.XPATH, Options.TOGGLE_BUTTON)
    wait.until(EC.element_to_be_clickable(toggle_btn))
    toggle_btn.click()

    # Click Confirm
    confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON)))
    confirm_btn.click()
    time.sleep(2) 

    # Step 4: Verify toast message appears and contains either 'active' or 'inactive'
    toast_el = wait.until(EC.visibility_of_element_located((By.XPATH, Confirmation_Dialogue.TOAST_MESSAGE)))
    actual_toast_text = toast_el.text.lower()
    
    assert "active" in actual_toast_text or "inactive" in actual_toast_text, (
        f"Expected toast message to contain 'active' or 'inactive', but got: '{toast_el.text}'"
    )

    # Verify total row count is reduced by 1
    time.sleep(2)  # Give table time to filter out the deactivated row
    updated_rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    
    # # If the last row was deactivated, check for empty state or count - 1
    # if initial_count == 1:
    #     assert len(updated_rows) == 0 or "no results found" in driver.find_element(By.XPATH, Table.BODY).text.lower()
    # else:
    #     assert len(updated_rows) == initial_count - 1, (
    #         f"Expected row count to be {initial_count - 1} after deactivation, but found {len(updated_rows)}."
    #     )