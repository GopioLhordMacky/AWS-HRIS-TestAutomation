from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page


@pytest.mark.NameError
def test_tc_fe_clients_052(authenticated_driver):
    """
    TC_FE_CLIENTS_052: (Functionality) Verify Active toggle default state for Active records
    
    1. Navigate to Clients page.
    2. Filter records by Status: Active (if filter dropdown is present).
    3. Iterate through rows in the table and verify Active toggle state is ON (True).
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Optional: If you have a status filter helper to ensure only Active records are shown
    # filter_by_status(driver, status="Active")

    target_column = "Active"
    TablePagination.change_rows_per_page(driver, 100)  
    time.sleep(2)  
    # Get total visible rows on current view\
    col_idx = TableData.get_column_index(driver, target_column)
    row_count = len(driver.find_elements(By.XPATH, f"//body/tr/td[{col_idx}]"))

    for row_idx in range(1, row_count + 1):
        is_active = FormControls.verify_active_toggle_state(driver, row_index=row_idx, column_name=target_column)
        assert is_active, f"Expected Active toggle to be ACTIVE for row {row_idx}, but found INACTIVE"


