from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import setup_browser, login_helper, open_add_fiscal_year_modal
from locators import Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_011(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    
    # Dynamic input string (Change this to any valid 'MM-YYYY')
    start_date = "05-2012"

    # Pre-condition: Open modal
    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    # 1. Dynamic Date Math & String Parsing
    dt = datetime.strptime(start_date, "%m-%Y")
    start_year = dt.year
    start_month = dt.month

    # Calculate end year dynamically based on 12-month period span
    end_year = start_year if start_month == 1 else start_year + 1

    # Formulate dynamic expected values
    expected_fy_name = f"{start_year}-{end_year}"
    expected_fy_code = f"FY{start_year}"

    # 2. Clear input cleanly & enter new date dynamically
    start_input = wait.until(EC.element_to_be_clickable((By.XPATH, Options.START_DATE)))
    
    # Using React Native Event Dispatcher so any MM-YYYY value is reliably registered
    driver.execute_script("""
        var input = arguments[0];
        var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(input, arguments[1]);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, start_input, start_date)

    # 3. Assert Fiscal Year and FY Code match dynamic calculations
    assert wait.until(
        EC.text_to_be_present_in_element_value((By.XPATH, Options.FY_NAME_INPUT), expected_fy_name)
    ), f"Expected Fiscal Year '{expected_fy_name}' for start month {start_date}."

    assert wait.until(
        EC.text_to_be_present_in_element_value((By.XPATH, Options.FY_CODE_INPUT), expected_fy_code)
    ), f"Expected FY Code '{expected_fy_code}' for start month {start_date}."