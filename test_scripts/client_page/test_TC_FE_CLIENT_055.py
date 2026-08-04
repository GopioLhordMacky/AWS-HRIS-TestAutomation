from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_055():
    """
    TC_FE_CLIENTS_055: (Functionality) Verify the Toggling Updates the Correct Client Record
    
    1. Filter by Status: Inactive using React-Select dropdown.
    2. Record initial pagination info using helper function.
    3. Toggle the active status for row 1 and click Confirm in the modal.
    4. Record updated pagination info using helper function.
    5. Assert that initial and updated pagination info are not equal.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Filter dropdown by "Inactive" status
    select_custom_dropdown(driver, "Status", "Inactive")
    time.sleep(2)

    # Step 2: Capture initial pagination count text via helper
    initial_pagination_info = get_pagination_information(driver)

    # Step 3: Toggle status on row 1
    toggle_active_status(driver, row_index=1, column_name="Active")
    
    # Confirm the status change in modal dialog
    click_confirm (driver)
    time.sleep(2)

    # Step 4: Capture updated pagination count text via helper
    updated_pagination_info = get_pagination_information(driver)

    # Step 5: Assertion
    assert initial_pagination_info != updated_pagination_info, (
        f"Pagination count did not update after toggling record status! "
        f"Initial: '{initial_pagination_info}' | Updated: '{updated_pagination_info}'"
    )

    close_browser(driver)