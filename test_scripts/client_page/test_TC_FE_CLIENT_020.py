from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_020(self, authenticated_driver):
        """Verify Default Selected Value in Industry Dropdown on Clients page."""
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(2)

        # Steps 1-4: Observe Industry dropdown default selection on the main Clients page table filter
        assert page.verify_industry_input_matches_client(expected_text="All"), "Default selected value in Industry dropdown does not match expected 'All Industries'."

    