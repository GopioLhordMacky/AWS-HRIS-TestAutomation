import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser
from locators import Buttons, Options, Confirmation_Dialogue

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_008(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # Pre-conditions: User logged in and "Add Fiscal Year" modal is open
    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    # Step 1: Leave Start Month empty (clear any existing text)
    start_date_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, Options.START_DATE))
    )
    
    # Select all and delete to guarantee the field is empty
    start_date_input.send_keys(Keys.CONTROL + "a")
    start_date_input.send_keys(Keys.BACKSPACE)

    # Step 2: Click the Save button
    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, Buttons.SAVE_BUTTON))
    )
    save_button.click()

    alert_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, Confirmation_Dialogue.START_DATE_REQUIRED))
    )
    assert alert_message.is_displayed(), "Validation alert message is not displayed."

    expected_text = "Start Date is required!".lower()
    actual_text = alert_message.text.lower()

    assert expected_text in actual_text, (
        f"Expected alert text containing '{expected_text}', but got '{actual_text}' (case-insensitive check)"
    )

    modal_title = driver.find_element(By.XPATH, "//div[@class='modal-content']")
    assert modal_title.is_displayed(), "Modal should remain open after validation error, but was closed."

    