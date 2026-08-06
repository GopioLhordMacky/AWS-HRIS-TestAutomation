import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_helper, open_add_fiscal_year_modal, setup_browser

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_002(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    login_helper(driver)
    open_add_fiscal_year_modal(driver)

    modal_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-title') or contains(text(), 'Add Fiscal Year')]"))
    )
    
    assert modal_header.is_displayed(), "Add Fiscal Year modal was not displayed."