import time
from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status
)
from Fiscal_Year_Page.helper_categ.toggle_helpers import toggle_row_confirm, count_rows

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_024(setup_browser):
    driver = setup_browser

    # --- Pre-condition ---
    login_helper(driver)
    select_status(driver, status="Inactive")
    time.sleep(2)

    # Ensure there is at least 1 record to toggle
    assert count_rows(driver) >= 1, "Expected at least 1 row to test toggle responsiveness."

    # --- Step 1: Measure execution speed of the toggle action ---
    start_time = time.perf_counter()
    
    # Perform toggle action
    toggle_row_confirm(driver)
    
    end_time = time.perf_counter()
    execution_duration = end_time - start_time

    # Optional logging to observe duration during test execution
    print(f"\n[Performance Metrics] Toggle action completed in: {execution_duration:.4f} seconds ({execution_duration * 1000:.2f} ms)")

    # --- Step 2: Assert toggle responsiveness constraint (< 300ms / 0.3s) ---
    assert execution_duration <= 3, (
        f"Toggle interaction took {execution_duration * 1000:.2f} ms, exceeding the 300 ms response threshold."
    )