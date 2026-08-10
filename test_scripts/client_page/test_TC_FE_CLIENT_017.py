
from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:
    def test_tc_fe_clients_017(self, authenticated_driver):
        """Verify that data in Add Client modal is cleared when closed and reopened."""
        page = go_to_client_page(authenticated_driver, via="url")

        # --- Pass 1: Close via Cancel Button ---
        # Steps 1–9: Open modal and enter valid data in all fields
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."

        assert page.fill_client_form(), "Failed to fill client form."

        # Step 10: Click Cancel/Close button inside modal footer
        assert page.click_close_modal_client(), "Failed to click the close button on the 'Add Client' modal."

        # Step 11: Reopen modal and verify fields are cleared
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        assert page.verify_client_modal_fields_are_empty(), \
            "Modal fields were not cleared after closing via Cancel button and reopening."

        # --- Pass 2: Close via Header 'X' / Close Button ---
        # Step 12: Enter valid data again
        assert page.fill_client_form(), "Failed to fill client form."

        # Step 13: Click the Close 'X' button in the modal header
        assert page.click_close_x_modal_client(), "Failed to click the close 'X' button in the modal header."

        # Step 14: Reopen modal and verify fields are cleared
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        assert page.verify_client_modal_fields_are_empty(), \
            "Modal fields were not cleared after closing via header 'X' button and reopening."

        # --- Pass 3: Close via Clicking Outside the Modal ---
        # Step 15: Enter valid data again
        assert page.fill_client_form(), "Failed to fill client form."

        # Step 16: Click outside the modal to close it
        assert page.click_outside_modal_client(), "Failed to click outside the modal to close it."

        # Step 17: Reopen modal and verify fields are cleared
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        assert page.verify_client_modal_fields_are_empty(), \
            "Modal fields were not cleared after closing via clicking outside modal and reopening."

        