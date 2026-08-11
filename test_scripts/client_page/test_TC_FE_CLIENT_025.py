from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    # @pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")
    def test_tc_fe_clients_025(self, authenticated_driver):
        """
        (Functionality) Verify Status Selection Filters Data in Table:
        1. Select 'Active' from the Status dropdown and observe table records.
        2. Select 'Inactive' from the Status dropdown and observe table records.
        3. Ensure table only displays records matching the selected status, hiding unselected ones.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1 & 2: Select "Active" and verify table filters to Active records only
        active_option = "Active"
        page.select_status_filter_client(option_text=active_option)

        assert page.check_toggle_status_on_table_client(
            column_name="Active",
            text=active_option
        ), f"Table failed to filter and display only '{active_option}' records."

        # Step 3 & 4: Select "Inactive" and verify table updates to Inactive records only
        inactive_option = "Inactive"
        page.select_status_filter_client(option_text=inactive_option)

        assert page.check_toggle_status_on_table_client(
             
            column_name="Active",
            text=inactive_option
        ), f"Table failed to filter and display only '{inactive_option}' records."
