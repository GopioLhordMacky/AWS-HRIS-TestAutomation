from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_043(self, authenticated_driver):
        """Verify the Industry dropdown displays the correct list of options."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open the "Add Client" modal
        page.click_edit_btn_by_row_index_client(row_idx=1)

        # Step 2: Verify the dropdown options list matches expected options

        assert page.verify_industry_dropdown_options(), "Industry dropdown options do not match expected list."

        # Step 4: Close the modal using click_close
        assert page.click_close_modal_client(), "Failed to close the modal"

        