from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_014(driver):
    """Verify Country Dropdown Data in Add Client Modal matches active countries in Location Management."""
    login_client_page(driver)
    time.sleep(3)

    # Step 1: Navigate to Location Management page to collect dynamic country data
    navigate_to_page(driver, "Location")
    time.sleep(3)
    
    # Store all country names from the "Location Name" / Country column
    expected_countries = TableData.check_column_cells(driver, "Location Name")

    # Step 2: Navigate to Client page
    navigate_to_page(driver, "Client")

    # Step 3: Open Add Client modal
    click_add_client_button(driver, timeout=10)

    # Step 4: Verify Country dropdown options match expected countries from Location Management
    assert ComponentVerifier.verify_dropdown_options(
        driver, 
        Update_Modal_Inputs.COUNTRY_SELECT, 
        expected_countries
    ), "Country dropdown options do not match active data in Location Management."

    driver.quit()