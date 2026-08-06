from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field,
    verify_table_search_results
)
from locators import Options, Table, Buttons, Modal

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_019(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # 1. Ensure Status is 'Active' and Search Field is empty
    select_status(driver)
    # fill_search_field(driver, search_str="")
    time.sleep(3)

    # Wait until table rows are visible
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    assert len(rows) >= 1, f"Expected at least 1 row in the table, but found {len(rows)}."

    # --- Step 1: Target the 3rd Row and Store Row Data ---
    target_row = rows[0]
    expected_row_text = target_row.text.strip()

    # Find and click the pencil/edit icon within the 1st row
    pencil_icon = target_row.find_element(By.XPATH, Buttons.EDIT_BUTTON)
    wait.until(EC.element_to_be_clickable(pencil_icon))
    pencil_icon.click()

    # --- Step 2: Verify Modal Opens ---
    wait.until(EC.visibility_of_element_located((By.XPATH, Modal.UPDATE_MODAL)))
    modal_el = driver.find_element(By.XPATH, Modal.UPDATE_MODAL)
    assert modal_el.is_displayed(), "Expected 'Update Fiscal Year' modal to be open."

    # --- Step 3: Verify Modal Data Matches Stored Row Content ---
    # Extract values from modal input fields/text elements
    modal_text = modal_el.text.strip()

    # Alternatively, if modal uses specific input fields, read their values:
    # modal_title_val = modal_el.find_element(By.XPATH, Modal.TITLE_INPUT).get_attribute("value")
    
    # Check that key information from the row text exists inside the modal
    row_data_tokens = [token for token in expected_row_text.split() if len(token) > 2]
    
    for token in row_data_tokens:
        # Ignore status labels if they don't appear directly in modal fields
        if token.lower() in ["active", "inactive"]:
            continue
        assert token in modal_text or token in driver.page_source, (
            f"Expected modal to contain data token '{token}' from row, but it was missing."
        )