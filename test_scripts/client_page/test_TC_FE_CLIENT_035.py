from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_035(self, authenticated_driver):
        """
        (UI/Design) Verify 'Add Client' Modal Components:
        1. Click "Edit Client" button.
        2. Verify modal title and container are visible.
        3. Verify all form fields (inputs and selects) are present.
        4. Verify action buttons (Close, Save) are present.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # 1. Click "Edit Client"
        page.click_edit_btn_by_row_index_client()  # Assuming the first row is used for testing

        # 2. Verify Modal Title & Container
        assert page.is_client_modal_visible_client(), "Expected 'Update Client' modal to be visible after clicking the Edit button, but it was not found."

        # 3. Verify Form Fields (Inputs & Selects)
        assert page.is_client_modal_inputs_visible_client(), "Expected input fields in 'Update Client' modal are missing."

        # 4. Verify Action Buttons
        assert page.is_client_modal_buttons_visible_client(), "Expected action buttons (Close, Save) in 'Update Client' modal are missing."