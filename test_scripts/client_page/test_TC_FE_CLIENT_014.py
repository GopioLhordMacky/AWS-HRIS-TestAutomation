from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_014(client_page):
    """Verify Country Dropdown Data in Add Client Modal matches active countries in Location Management."""
    page = client_page

    time.sleep(3)

    # Step 1: Navigate to Location Management page to collect dynamic country data
    page.navigate_to_page(  "Location")
    time.sleep(3)
    
    # Store all country names from the "Location Name" / Country column
    expected_countries = page.check_column_cells(  "Location Name")

    # Step 2: Navigate to Client page
    page.navigate_to_page(  "Client")

    # Step 3: Open Add Client modal
    page.click_add_client_button()

    # Step 4: Verify Country dropdown options match expected countries from Location Management
    assert page.verify_dropdown_options(
          
        Update_Modal_Inputs.COUNTRY_SELECT, 
        expected_countries
    ), "Country dropdown options do not match active data in Location Management."

    