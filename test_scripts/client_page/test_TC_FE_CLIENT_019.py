import time
from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_019(self, authenticated_driver):
        """Verify the Industry dropdown displays the correct list of options."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open the "Add Client" modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."

        # Step 2: Verify the dropdown options list matches expected options
        assert page.verify_industry_dropdown_options()," Industry dropdown options do not match expected options."

        # Step 3: Select an option ("Automotive") using react dropdown helper
        time.sleep(3)
        assert page.fill_industry_select_modal_client(), "Failed to fill industry dropdown."

        # Step 4: Close the modal using click_close
        assert page.click_close_modal_client(), "Failed to close the 'Add Client' modal."
