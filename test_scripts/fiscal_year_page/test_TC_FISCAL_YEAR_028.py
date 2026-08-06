import time
from plugins import *
from Fiscal_Year_Page.helper_categ.pagination_helpers import (
    get_pagination_text,
    go_to_next_page,
    go_to_previous_page,
    get_first_row_text,
    is_button_disabled
)
from helpers import *
from locators import Pagination

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_028(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(2)

    # --- Step 1: Verify Previous (<) button is disabled on Page 1 ---
    prev_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON))
    )
    assert is_button_disabled(prev_btn), (
        "Expected Previous ('<') button to be disabled on the first page."
    )

    # Verify Next (>) button is enabled on Page 1
    next_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, Pagination.NEXT_PAGE_BUTTON))
    )
    assert not is_button_disabled(next_btn), (
        "Expected Next ('>') button to be enabled when more pages exist."
    )

    # --- Step 2: Navigate to the last page ---
    max_pages = 20  # Safety cap to prevent infinite loops
    page_count = 0

    while not is_button_disabled(next_btn) and page_count < max_pages:
        go_to_next_page(driver)
        next_btn = driver.find_element(By.XPATH, Pagination.NEXT_PAGE_BUTTON)
        page_count += 1

    # --- Step 3: Verify Next (>) button is disabled on the last page ---
    assert is_button_disabled(next_btn), (
        "Expected Next ('>') button to be disabled on the last page."
    )

    # Verify Previous (<) button is now enabled on the last page
    prev_btn = driver.find_element(By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON)
    assert not is_button_disabled(prev_btn), (
        "Expected Previous ('<') button to be enabled on the last page."
    )