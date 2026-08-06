from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser
from locators import Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_010(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    
    # Dynamic input string (Change this to any 'MM-YYYY')
    start_date = "12-2021"

    # Pre-condition: Open modal
    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    # 1. Clear input & trigger React state change dynamically via JS
    start_input = wait.until(EC.presence_of_element_located((By.XPATH, Options.START_DATE)))
    
    driver.execute_script("""
        var input = arguments[0];
        var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(input, arguments[1]);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, start_input, start_date)

    # 2. Dynamic Date Math (Calculates exactly +11 months to complete a 12-month period)
    dt = datetime.strptime(start_date, "%m-%Y")
    expected_year = dt.year if dt.month == 1 else dt.year + 1
    expected_month = 12 if dt.month == 1 else dt.month - 1
    expected_end = f"{expected_month:02d}-{expected_year}"

    # 3. Assert auto-populated End Date matches dynamic 12-month calculation
    assert wait.until(
        EC.text_to_be_present_in_element_value((By.XPATH, Options.END_DATE), expected_end)
    ), f"End Date boundary check failed. Expected '{expected_end}' for start month {start_date}."