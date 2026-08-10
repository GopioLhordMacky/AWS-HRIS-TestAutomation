from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_018(self, authenticated_driver):
        """Verify 'Add Client' Modal Closes When Clicking Outside of the Modal."""
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open the "Add Client" modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        
        # Fill out the form to test that entered data is not persisted
        assert page.fill_client_form(), "Failed to fill the 'Add Client' modal."

        # Step 2: Click outside the modal to close it
        assert page.click_outside_modal_client(), "Failed to click outside the 'Add Client' modal."

        # Verification: Reopen the modal and verify all fields are cleared (data was not saved)
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        assert page.verify_client_modal_fields_are_empty(), "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

        