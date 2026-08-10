from data.client_page_inputs import Options
from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_023(self, authenticated_driver):
        """
        (Functionality) Verify the Status dropdown displays the correct list of options 
        ('Active', 'Inactive') and can select an option.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(1)

        # Step 1 & 2: Verify that the Status dropdown displays the correct list of options
        assert page.verify_status_dropdown_options(), f"Expected Status dropdown options not found mismatching options."
        
        # Step 3: Select 'Active' from dropdown and verify filtering on toggle column
        target_option = "Active"
        page.select_status_filter_client(target_option)
        time.sleep(3)

        # Validate that the selected option filters the table properly
        ## THIS IS NOT WORKING, SINCE BOTH ACTIVE AND INACTIVE HAS 'checked' ATTRIBUTE ##
        assert page.check_toggle_status_on_table_client(
            column_name="Active",
            text=target_option
        ), f"Table did not properly update to reflect selected Status option: '{target_option}'"

        time.sleep(3)
    