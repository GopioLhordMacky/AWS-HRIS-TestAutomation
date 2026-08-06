import pytest
from plugins import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import (
    setup_browser, 
    login_helper, 
    open_add_fiscal_year_modal, 
    fill_start_date,
    select_status
)
from locators import Options, Table, Buttons, Confirmation_Dialogue

## This test might fail if the helpers are not updated to input unlisted Start Date 

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_012(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    # --- Step 1: Select a valid Start Month ---
    fill_start_date(driver, date_str= FillStartDate.date_str)  

    # --- Step 2: Verify auto-populated fields in the modal ---
    start_date_val = driver.find_element(By.XPATH, Options.START_DATE).get_attribute("value")
    end_date_val = driver.find_element(By.XPATH, Options.END_DATE).get_attribute("value")
    fy_name_val = driver.find_element(By.XPATH, Options.FY_NAME_INPUT).get_attribute("value")
    fy_code_val = driver.find_element(By.XPATH, Options.FY_CODE_INPUT).get_attribute("value")

    assert end_date_val != "", "End Date should be automatically populated."
    assert fy_name_val != "", "Fiscal Year name should be automatically populated."
    assert fy_code_val != "", "FY Code should be automatically populated."

    # --- Step 3: Click the "Save" button ---
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.SAVE_BUTTON)))
    save_btn.click()

    # --- Step 4: Observe confirmation message and verify created record ---
    # 1. Verify Toast Message
    toast_element = wait.until(EC.visibility_of_element_located((By.XPATH, Confirmation_Dialogue.TOAST_MESSAGE)))
    assert "Fiscal year registered successfully" in toast_element.text, \
        f"Expected toast message not found. Got: {toast_element.text}"

    # 2. Verify modal closes & record is present in table
    wait.until(EC.invisibility_of_element_located((By.XPATH, Options.START_DATE)))

    select_status(driver,status="Active")
    time.sleep(2)
    # Wait until table rows exist using your Table class
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    
    table_content = driver.find_element(By.XPATH, "//tbody").text
    assert fy_code_val in table_content, f"FY Code '{fy_code_val}' not found in Fiscal Year table."
    assert fy_name_val in table_content, f"Fiscal Year '{fy_name_val}' not found in Fiscal Year table."