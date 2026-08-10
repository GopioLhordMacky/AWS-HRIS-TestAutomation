import time
from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_client_001(self, authenticated_driver):
        """TC_FE_CLIENTS_001: Verify the '+ Add Client' button opens the 'Add Client' modal."""
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(2)

        # Step 1: Click the "+ Add Client" button
        assert  page.click_add_client_button(), "Failed to click the '+ Add Client' button on the client page."

        # Step 2: Verify the "Add Client" modal pops up
        assert page.is_client_modal_visible(), "The 'Add Client' modal failed to pop up."



