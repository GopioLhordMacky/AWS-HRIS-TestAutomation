from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")
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
    select_custom_dropdown(driver, "Status", "Active")
    time.sleep(2)

    target_column = "Active"
    
    # Step 1 & 2: Check each row to confirm the toggle state is active/ON
    assert check_toggle_status_on_table(
        driver,
        column_name="Active",
        text="Inactive"
    ), f"Table failed to filter and display only '{target_column}' records."

    close_browser(driver)