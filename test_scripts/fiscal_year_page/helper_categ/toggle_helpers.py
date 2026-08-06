import pytest
from plugins import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Fiscal_Year_Page.locators import Login_Locators, Sidebar_Locators, Buttons, Options, Table, Confirmation_Dialogue

def count_rows(driver):
    """
    Waits for the table rows to be present, retrieves all row elements, 
    and returns the total row count.
    """
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    return len(rows)


def toggle_row_confirm(driver, status="Active", row_index=0):
    """
    Selects the status, targets a specific row by index to click its toggle button, 
    clicks Confirm in the dialogue, and verifies the active/inactive toast message.
    """
    wait = WebDriverWait(driver, 10)


    # 2. Locate target row and toggle button
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    target_row = rows[row_index]
    
    toggle_btn = target_row.find_element(By.XPATH, Options.TOGGLE_BUTTON)
    wait.until(EC.element_to_be_clickable(toggle_btn))
    toggle_btn.click()

    # 3. Confirm action
    confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON)))
    confirm_btn.click()
    time.sleep(2)

    # 4. Verify toast message
    toast_el = wait.until(EC.visibility_of_element_located((By.XPATH, Confirmation_Dialogue.TOAST_MESSAGE)))
    actual_toast_text = toast_el.text.lower()
    
    assert "active" in actual_toast_text or "inactive" in actual_toast_text, (
        f"Expected toast message to contain 'active' or 'inactive', but got: '{toast_el.text}'"
    )

def toggle_row_cancel(driver, status="Active", row_index=0):
    """
    Selects the status, targets a specific row by index to click its toggle button, 
    verifies confirmation dialogue buttons appear, and clicks Cancel.
    """
    wait = WebDriverWait(driver, 10)

    # 1. Select status and wait for table to settle
    select_status(driver, status=status)
    time.sleep(3)

    # 2. Locate target row and toggle button
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    target_row = rows[row_index]

    toggle_btn = target_row.find_element(By.XPATH, Options.TOGGLE_BUTTON)
    wait.until(EC.element_to_be_clickable(toggle_btn))
    toggle_btn.click()

    # 3. Verify confirmation dialogue options appear
    cancel_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CANCEL_BUTTON)))
    confirm_btn = driver.find_element(By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON)
    assert confirm_btn.is_displayed(), "Expected 'Confirm' button to be visible."
    assert cancel_btn.is_displayed(), "Expected 'Cancel' button to be visible."

    # 4. Click Cancel
    cancel_btn.click()
    time.sleep(2)