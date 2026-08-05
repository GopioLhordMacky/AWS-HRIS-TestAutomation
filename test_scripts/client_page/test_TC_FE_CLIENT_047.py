from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_048(authenticated_driver):
    """
    TC_FE_CLIENTS_048: Verify Column Sorting in Ascending Order (Client Page)
    
    1. Navigate to Client Page.
    2. Expand rows per page view to 100 to show max data entries.
    3. Click column header to trigger sort.
    4. Verify column contents display in ascending order.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    column_to_sort = "Client Name"

    # Step 1: Change rows per page to 100
    change_rows_per_page(driver, 100)

    # Step 2 & 3: Trigger sort and verify ascending order
    verify_column_sorting(driver, column_to_sort, order="ascending")

    close_browser(driver)