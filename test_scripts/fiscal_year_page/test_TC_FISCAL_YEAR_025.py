import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from plugins import *
from helpers import setup_browser, login_helper, select_status
from locators import Confirmation_Dialogue, Table, Options

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_025(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(2)

    # Step 1: Navigate to the first toggle button using TAB navigation
    # We first target an element above the table or inside the page to establish base focus
    actions = ActionChains(driver)

    # Alternatively, locate the toggle element directly to verify focus transition
    toggle_element = wait.until(
        EC.presence_of_element_located((By.XPATH, f"({Table.TABLE_ROWS})[1]{Options.TOGGLE_BUTTON}"))
    )

    # Tab loop until focused element matches target toggle
    max_tabs = 20
    is_focused = False

    for _ in range(max_tabs):
        actions.send_keys(Keys.TAB).perform()
        focused_element = driver.switch_to.active_element
        if focused_element == toggle_element or focused_element.find_elements(By.XPATH, ".//ancestor-or-self::*[contains(@class, 'MuiSwitch-root')]"):
            is_focused = True
            break

    assert is_focused, "Toggle button was not reachable using the TAB key."

    # Step 2: Press SPACE key on the focused toggle
    actions.send_keys(Keys.SPACE).perform()

    # Step 3: Verify confirmation dialogue appears
    confirm_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, Confirmation_Dialogue.CONFIRM_BUTTON))
    )
    assert confirm_btn.is_displayed(), "Expected confirmation modal to appear after pressing SPACE."

    # Step 4: Click Confirm
    confirm_btn.click()
    time.sleep(2)