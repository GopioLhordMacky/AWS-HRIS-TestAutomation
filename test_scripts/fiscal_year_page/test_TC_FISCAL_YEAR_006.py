import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Fiscal_Year_Page.locators import Buttons
from helpers import login_helper, setup_browser

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_006(setup_browser):
    """
    TC_FE_FISCAL_YEAR_006 (Accessibility)
    Verify that the '+ Add Fiscal Year' button can be focused using TAB 
    and opened using SPACE/ENTER key.
    """
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # Pre-condition: User logged in and Fiscal Year page displayed
    login_helper(driver)

    # Wait for the Add Fiscal Year button to be present on the page
    add_button = wait.until(EC.presence_of_element_located((By.XPATH, Buttons.ADD_FISCAL_YEAR_BUTTON)))

    # Step 1: Press TAB until the Add Fiscal Year button is focused
    # Starting tab navigation from the page body
    active_element = driver.switch_to.active_element
    max_tabs = 30  # Safety limit to prevent infinite loop
    tab_count = 0
    button_focused = False

    while tab_count < max_tabs:
        active_element.send_keys(Keys.TAB)
        active_element = driver.switch_to.active_element
        
        # Check if the currently focused element matches the Add Fiscal Year button
        if active_element == add_button:
            button_focused = True
            break
        tab_count += 1

    assert button_focused, "Add Fiscal Year button was not reached using TAB navigation."

    # Step 2: Press ENTER to open the modal
    active_element.send_keys(Keys.ENTER)

    # Step 3: Observe if the Add Fiscal Year modal opens
    modal_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-title') or contains(text(), 'Add Fiscal Year')]"))
    )
    assert modal_title.is_displayed(), "The 'Add Fiscal Year' modal did not open when pressing ENTER on the focused button."