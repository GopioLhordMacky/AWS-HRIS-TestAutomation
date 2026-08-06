import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_005(setup_browser):
    """
    TC_FE_FISCAL_YEAR_005 (Functional)
    Verify that clicking the '+ Add Fiscal Year' button opens the Add Fiscal Year modal pop-up.
    """
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    login_helper(driver)

    open_add_fiscal_year_modal(driver)

    # Verification: 'Add Fiscal Year' modal popped up successfully
    modal_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-body') or contains(text(), 'Add Fiscal Year')]"))
    )
    assert modal_title.is_displayed(), "The 'Add Fiscal Year' modal did not pop up after clicking the button."