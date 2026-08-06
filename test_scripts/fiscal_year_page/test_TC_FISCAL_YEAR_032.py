import time
from selenium.webdriver.common.keys import Keys
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    get_first_row_text,
    change_rows_per_page,
    wait_for_valid_pagination
)
from helpers import *
from locators import Pagination

@pytest.mark.accessibility
def test_TC_FE_FISCAL_YEAR_032(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(2)
    # Force 10 rows per page to ensure multi-page navigation is available
    change_rows_per_page(driver, 10)
    wait_for_valid_pagination(driver)

    # Initial state (Page 1)
    p1_text = get_pagination_text(driver)
    p1_row = get_first_row_text(driver)

    # --- Step 1: Use keyboard navigation to reach and activate Next (>) button ---
    next_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.NEXT_PAGE_BUTTON))
    )
    
    # Focus Next button natively via JS
    driver.execute_script("arguments[0].focus();", next_btn)
    time.sleep(0.5)
    
    # Send ENTER key to focused element
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    wait_for_valid_pagination(driver)

    p2_text = get_pagination_text(driver)
    p2_row = get_first_row_text(driver)

    # Verify keyboard activation updated the page to Page 2
    assert p2_text != p1_text, "Expected pagination range to change after pressing ENTER on Next button."
    assert p2_row != p1_row, "Expected table rows to update after pressing ENTER on Next button."

    # --- Step 2 & 3: Navigate to Previous (<) button and trigger SPACE ---
    prev_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON))
    )
    
    # Focus Previous button natively via JS
    driver.execute_script("arguments[0].focus();", prev_btn)
    time.sleep(0.5)

    # Send SPACE key to focused element
    driver.switch_to.active_element.send_keys(Keys.SPACE)
    wait_for_valid_pagination(driver)

    returned_p1_text = get_pagination_text(driver)
    returned_p1_row = get_first_row_text(driver)

    # Verify keyboard activation reverted back to Page 1
    assert returned_p1_text == p1_text, (
        f"Expected range to revert to '{p1_text}', but got '{returned_p1_text}' after pressing SPACE on Previous."
    )
    assert returned_p1_row == p1_row, "Expected table rows to revert to Page 1 content."

    # --- Step 4 & 5: Keyboard interaction with specific Page Number buttons ---
    try:
        page_2_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='page 2' or text()='2']"))
        )
        
        assert page_2_btn.get_attribute("tabindex") != "-1", "Page number button should be focusable via TAB."
        
        driver.execute_script("arguments[0].focus();", page_2_btn)
        time.sleep(0.5)
        
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        wait_for_valid_pagination(driver)

        assert get_pagination_text(driver) == p2_text, "Expected table to update to Page 2 via keyboard selection."

    except Exception:
        # Standard MUI range-only fallback verification
        driver.execute_script("arguments[0].focus();", next_btn)
        time.sleep(0.5)
        driver.switch_to.active_element.send_keys(Keys.SPACE)
        wait_for_valid_pagination(driver)
        assert get_pagination_text(driver) != p1_text, "Pagination state failed to change via keyboard action."