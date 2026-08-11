from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page
class TestClientPage:
    
    def test_tc_fe_clients_044(self, authenticated_driver):
        """Verify Country Dropdown Data in Add Client Modal matches active countries in Location Management."""
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(3)

        # Step 1: Navigate to Location Management page to collect dynamic country data
        assert page.navigate_to_page("Location"), "Failed to navigate to Location "
        time.sleep(3)
        
        # Store all country names from the "Location Name" / Country column
        expected_countries = page.check_column_cells_client("Location Name")

        # Step 2: Navigate to Client page
        assert page.navigate_to_page("Client"), "Failed to go to Client page"

        # Step 3: Open Add Client modal
        assert page.click_edit_btn_by_row_index_client(), "Failed to click Edit Button"

        # Step 4: Verify Country dropdown options match expected countries from Location Management
        assert page.verify_country_dropdown_options(expected_options=expected_countries), "Country on Location page does not match options in Country dropdown"

        