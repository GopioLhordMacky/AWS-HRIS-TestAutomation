from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


def test_tc_fe_clients_048(client_page):
    """
    TC_FE_CLIENTS_048: Verify Column Sorting in Ascending Order (Client Page)
    
    1. Navigate to Client Page.
    2. Expand rows per page view to 100 to show max data entries.
    3. Click column header to trigger sort.
    4. Verify column contents display in ascending order.
    """
    page = client_page

    column_to_sort = "Client Name"

    # Step 1: Change rows per page to 100
    page.change_rows_per_page(  100)

    # Step 2 & 3: Trigger sort and verify ascending order
    page.verify_column_sorting(  column_to_sort, order="ascending")

    