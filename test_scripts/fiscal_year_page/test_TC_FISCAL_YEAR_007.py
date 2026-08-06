import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser, close_btn
from locators import Buttons, Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_007(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # Pre-condition: User logged in and Fiscal Year page displayed
    login_helper(driver)

    # Step 1 & 2: Click "+ Add Fiscal Year" to open the modal
    open_add_fiscal_year_modal(driver)

    # Step 3: Verify Modal Components

    # 1. Modal Title
    modal_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class = 'modal-title h4']"))
    )
    assert modal_title.is_displayed(), "Modal title 'Add Fiscal Year' is not displayed."

    # 2. Start Month Label, Required Indicator (*), and Input/Icon
    start_date_label = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Start Date')]"))
    )
    assert start_date_label.is_displayed(), "Start Date label is not displayed."


    # Verify Start Date input field & Calendar Icon
    start_date_input = driver.find_element(By.XPATH, Options.START_DATE)
    assert start_date_input.is_displayed(), "Start Date input box is not displayed."

    # 3. End Month Label and Disabled Date Picker Input
    end_date_input = driver.find_element(
        By.XPATH, Options.END_DATE
    )
    assert not end_date_input.is_enabled() or end_date_input.get_attribute("disabled") is not None, "End Month field should be disabled."

    # 4. Fiscal Year Label and Disabled Input box
    fy_name_input = driver.find_element(
        By.XPATH, Options.FY_NAME_INPUT
    )
    assert not fy_name_input.is_enabled() or fy_name_input.get_attribute("disabled") is not None, "Fiscal Year field should be disabled."

    # 5. FY Code Label and Disabled Input box
    fy_code_input = driver.find_element(
        By.XPATH, Options.FY_CODE_INPUT
    )
    assert not fy_code_input.is_enabled() or fy_code_input.get_attribute("disabled") is not None, "FY Code field should be disabled."

    # 6. Close / Cancel Button
    close_button = driver.find_element(
        By.XPATH, Buttons.CLOSE_BUTTON
    )
    assert close_button.is_displayed(), "Close/Cancel button is not displayed on the modal."

    # 7. Save Button
    save_button = driver.find_element(
        By.XPATH, Buttons.SAVE_BUTTON
    )
    assert save_button.is_displayed(), "Save button is not displayed on the modal."