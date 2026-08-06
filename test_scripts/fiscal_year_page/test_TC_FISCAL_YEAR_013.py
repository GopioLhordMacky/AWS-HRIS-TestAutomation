import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import (
    setup_browser, 
    login_helper, 
    open_add_fiscal_year_modal, 
    fill_start_date, 
    close_btn, 
    close_by_x_btn, 
    close_by_backdrop
)
from locators import Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_013(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # Pre-condition
    login_helper(driver)

    # --- Step 1: Close via 'Close' Button ---
    open_add_fiscal_year_modal(driver)
    fill_start_date(driver, date_str="11-1991")  
    close_btn(driver)
    
    # Reopen and verify fields reset to empty / default state
    open_add_fiscal_year_modal(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, Options.START_DATE)))
    
    assert driver.find_element(By.XPATH, Options.START_DATE).get_attribute("value") == ""
    assert driver.find_element(By.XPATH, Options.FY_NAME_INPUT).get_attribute("value") == ""
    assert driver.find_element(By.XPATH, Options.FY_CODE_INPUT).get_attribute("value") == ""

    # --- Step 2: Close via 'X' Header Icon ---
    fill_start_date(driver)
    close_by_x_btn(driver)
    
    # Reopen and verify fields reset to empty / default state
    open_add_fiscal_year_modal(driver)
    wait.until(EC.visibility_of_element_located((By.XPATH, Options.START_DATE)))
    
    assert driver.find_element(By.XPATH, Options.START_DATE).get_attribute("value") == ""
    assert driver.find_element(By.XPATH, Options.FY_NAME_INPUT).get_attribute("value") == ""
    assert driver.find_element(By.XPATH, Options.FY_CODE_INPUT).get_attribute("value") == ""

    ### THIS IS NOT WORKING DUE TO XPATH FAILURE###
    # To fix go to: helpers.py >> close_by_dropback [Then use working XPATH]

    # # --- Step 3: Close via Backdrop Click ---
    # fill_start_date(driver)
    # close_by_backdrop(driver)
    
    # # Reopen and verify fields reset to empty / default state
    # open_add_fiscal_year_modal(driver)
    # wait.until(EC.visibility_of_element_located((By.XPATH, Options.START_DATE)))
    
    # assert driver.find_element(By.XPATH, Options.START_DATE).get_attribute("value") == ""
    # assert driver.find_element(By.XPATH, Options.FY_NAME_INPUT).get_attribute("value") == ""
    # assert driver.find_element(By.XPATH, Options.FY_CODE_INPUT).get_attribute("value") == ""