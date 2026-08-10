from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_014(self, authenticated_driver):
        """Verify Country Dropdown Data in Add Client Modal matches active countries in Location Management."""
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(3)

        # Step 1: Navigate to Location Management page to collect dynamic country data
        assert page.navigate_to_page("Location")," Failed to navigate to the 'Location' page from the sidebar."
        time.sleep(3)
        
        # Store all country names from the "Location Name" / Country column
        expected_countries = page.check_column_cells_client("Location Name")

        # Step 2: Navigate to Client page
        assert page.navigate_to_page("Client"), "Failed to navigate to the 'Client' page from the sidebar."

        # Step 3: Open Add Client modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."

        # Step 4: Verify Country dropdown options match expected countries from Location Management
        assert page.verify_country_dropdown_options(expected_options=expected_countries), "Country dropdown options do not match active countries in Location Management."

        