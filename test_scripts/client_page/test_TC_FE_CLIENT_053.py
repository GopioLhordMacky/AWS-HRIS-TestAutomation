from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


# @pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")
def test_tc_fe_clients_053(client_page):
    """
    TC_FE_CLIENTS_053: (Functionality) Verify Active toggle default state for Active records
    
    1. Navigate to Clients page.
    2. Filter records by Status: Active (if filter dropdown is present).
    3. Iterate through rows in the table and verify Active toggle state is ON (True).
    """
    page = client_page


    # Optional: If you have a status filter helper to ensure only Active records are shown
    page.select_custom_dropdown(  "Status", "Active")
    time.sleep(2)

    target_column = "Active"
    
    # Step 1 & 2: Check each row to confirm the toggle state is active/ON
    assert page.check_toggle_status_on_table(
         
        column_name="Active",
        text="Inactive"
    ), f"Table failed to filter and display only '{target_column}' records."

