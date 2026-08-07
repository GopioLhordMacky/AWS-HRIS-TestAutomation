from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_005(self, authenticated_driver):
        """TC_FE_CLIENTS_005: Verify the '+ Add Client' button opens the 'Add Client' modal."""
        page = go_to_client_page (authenticated_driver, via="url")

        # Step 1: Click the "+ Add Client" button
        page.click_add_client_button()

        # Step 2: Verify the "Add Client" modal pops up
        assert page.is_client_modal_visible(), "The 'Add Client' modal failed to pop up."