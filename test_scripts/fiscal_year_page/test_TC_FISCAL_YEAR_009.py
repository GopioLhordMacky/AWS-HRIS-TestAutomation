import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser
from locators import Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_009(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # Pre-conditions: User logged in and "Add Fiscal Year" modal open
    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    # Step 1 & 2: Click Start Month date picker and select/enter "04-2026"
    start_date_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, Options.START_DATE))
    )
    start_date_input.click()
    start_date_input.send_keys(Keys.CONTROL + "a")
    start_date_input.send_keys(Keys.BACKSPACE)
    start_date_input.send_keys("04-2026")
    start_date_input.send_keys(Keys.RETURN)


    # Expected Result 1: End Date auto-populates to "03-2027"
    end_date_input = driver.find_element(By.XPATH, Options.END_DATE)
    actual_end_date = end_date_input.get_attribute("value")
    assert actual_end_date == "03-2027", (
        f"Expected End Date '03-2027', but got '{actual_end_date}'"
    )

    # Expected Result 2: Fiscal Year auto-populates to "2026-2027"
    fy_name_input = driver.find_element(By.XPATH, Options.FY_NAME_INPUT)
    actual_fy_name = fy_name_input.get_attribute("value")
    assert actual_fy_name == "2026-2027", (
        f"Expected Fiscal Year '2026-2027', but got '{actual_fy_name}'"
    )

    # Expected Result 3: FY Code auto-populates to "FY2026"
    fy_code_input = driver.find_element(By.XPATH, Options.FY_CODE_INPUT)
    actual_fy_code = fy_code_input.get_attribute("value")
    assert actual_fy_code == "FY2026", (
        f"Expected FY Code 'FY2026', but got '{actual_fy_code}'"
    )

    # Expected Result 4: Ensure auto-populated fields remain disabled / read-only (no manual input allowed)
    for field, name in [
        (end_date_input, "End Date"),
        (fy_name_input, "Fiscal Year"),
        (fy_code_input, "FY Code"),
    ]:
        assert not field.is_enabled() or field.get_attribute("disabled") is not None, (
            f"{name} field should be disabled for manual input."
        )