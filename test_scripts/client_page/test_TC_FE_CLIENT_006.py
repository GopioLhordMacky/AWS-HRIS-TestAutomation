from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_006(self, authenticated_driver):
        """TC_FE_CLIENTS_006: Verify UI design and visibility of 'Add Client' modal components."""
        page = go_to_client_page (authenticated_driver, via="url")

        # 1. Click "+ Add Client"
        page.click_add_client_button()

        # 2. Verify Modal Title & Container
        assert page.is_client_modal_inputs_visible(), "Failed to display all required input fields in the 'Add Client' modal."
        assert page.is_client_modal_buttons_visible(), "Failed to display all required action buttons in the 'Add Client' modal."

