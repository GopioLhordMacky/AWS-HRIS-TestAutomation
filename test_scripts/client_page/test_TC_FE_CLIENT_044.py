from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_044():
    """Verify Country Dropdown Data in Add Client Modal matches active countries in Location Management."""
    driver = open_browser("chrome")
    login_client_page(driver)
    time.sleep(3)

    # Step 1: Navigate to Location Management page to collect dynamic country data
    navigate_to_page(driver, "Location")
    time.sleep(3)
    
    # Store all country names from the "Location Name" / Country column
    expected_countries = check_column_cells(driver, "Location Name")

    # Step 2: Navigate to Client page
    navigate_to_page(driver, "Client")

    # Step 3: Open Add Client modal
    click_edit_btn_by_row_index(driver, row_idx=1)

    # Step 4: Verify Country dropdown options match expected countries from Location Management
    assert verify_dropdown_options(
        driver, 
        Update_Modal_Inputs.COUNTRY_SELECT, 
        expected_countries
    ), "Country dropdown options do not match active data in Location Management."

    close_browser(driver)