from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field,
    update_start_date,
    click_edit_fiscal_year,
    save_btn
    
)
from locators import Options, Table, Buttons, Modal, Confirmation_Dialogue

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_020(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    time.sleep(5)

    # --- Step 1: Locate an existing record and click Edit ---
    click_edit_fiscal_year(driver)

    # --- Step 2: Modal opens ---
    wait.until(EC.visibility_of_element_located((By.XPATH, Modal.UPDATE_MODAL)))

    # --- Step 3: Update Start Month ---
    new_date = update_start_date(driver, date_str= UpdateStartDate.date_string)  

    # --- Step 4: Verify auto-recalculation in dependent fields ---
    # Give React a split second to compute dependent field state
    time.sleep(0.5)

    end_date_val = driver.find_element(By.XPATH, Options.END_DATE).get_attribute("value")
    fy_code_val = driver.find_element(By.XPATH, Options.FY_CODE_INPUT).get_attribute("value")
    fiscal_year_val = driver.find_element(By.XPATH, Options.FY_NAME_INPUT).get_attribute("value")

    assert end_date_val != "", "Expected End Date to be auto-recalculated, but it was empty."
    assert fy_code_val != "", "Expected FY Code to be auto-recalculated, but it was empty."
    assert fiscal_year_val != "", "Expected Fiscal Year to be auto-recalculated, but it was empty."

    # --- Step 5: Click Save ---
    save_btn(driver)

    # --- Step 6: Click Confirm via helper ---
    confirm_update = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON))).click()

    # --- Step 7: Verify Toast & Modal closure ---
    toast_el = wait.until(EC.visibility_of_element_located((By.XPATH, Confirmation_Dialogue.TOAST_MESSAGE)))
    assert "Fiscal year updated successfully!" in toast_el.text, (
        f"Expected success toast message, but got: '{toast_el.text}'"
    )

    wait.until(EC.invisibility_of_element_located((By.XPATH, Modal.UPDATE_MODAL)))

    # --- Step 8: Verify table reflects updated data ---
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    updated_rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    table_text = " ".join([row.text for row in updated_rows])

    assert new_date in table_text or fiscal_year_val in table_text, (
        f"Expected updated start date '{new_date}' or fiscal year '{fiscal_year_val}' to appear in the table."
    )