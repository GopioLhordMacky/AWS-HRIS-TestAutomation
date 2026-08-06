from plugins import *
from helpers import (
    setup_browser, 
    login_helper, 
    select_status, 
    fill_search_field
)
from locators import Table, Buttons

@pytest.mark.functionality
def test_TC_FE_FISCAL_YEAR_021(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    # --- Pre-condition ---
    login_helper(driver)

    # Ensure table rows are loaded
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))

    # --- Step 1: Click column header / sort button ---
    sort_header = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.SORT_BUTTON)))    
    sort_header.click()

   # --- Step 2: Validate First Sort Direction ---
    # Brief wait for sorting re-render
    time.sleep(5)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows_after_first_click = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    
    # Safely extract text from non-empty rows
    first_click_data = [
        row.text.split()[0] for row in rows_after_first_click if row.text.strip()
    ]
    assert len(first_click_data) > 0, "Expected table rows with text data after sorting."

    # Verify data is sorted (either ascending or descending)
    is_asc = first_click_data == sorted(first_click_data)
    is_desc = first_click_data == sorted(first_click_data, reverse=True)
    assert is_asc or is_desc, f"Table data was not properly sorted. Current order: {first_click_data}"

    # --- Step 3: Click again to toggle sort direction ---
    sort_header = wait.until(EC.element_to_be_clickable((By.XPATH, Buttons.SORT_BUTTON)))    
    sort_header.click()
    time.sleep(2)


    # --- Step 4: Validate Reversed Sort Direction ---
    wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    rows_after_second_click = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    second_click_data = [row.text.split()[0] for row in rows_after_second_click]

    if is_asc:
        assert second_click_data == sorted(second_click_data, reverse=True), (
            f"Expected table to be sorted descending, but got: {second_click_data}"
        )
    else:
        assert second_click_data == sorted(second_click_data), (
            f"Expected table to be sorted ascending, but got: {second_click_data}"
        )