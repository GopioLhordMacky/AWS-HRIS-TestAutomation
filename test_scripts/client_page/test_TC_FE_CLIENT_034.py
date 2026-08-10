from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:
    def test_tc_fe_clients_034(self, authenticated_driver):
        """
        (Functionality) Verify the Edit/Pencil button opens the "Update Client" modal:
        1. Click the Edit/Pencil button for a specific record.
        2. Verify the "Update Client" modal is displayed/visible.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Click the Edit button for a specific record in the table
        page.change_rows_per_page_client(100)
        time.sleep(2)
        page.click_edit_btn_by_column_value_client("Contact Person", "John Doe")

        # Step 2: Verify the Update Client modal pops up
        assert page.is_client_modal_visible(), "Expected 'Update Client' modal to be visible after clicking the Edit button, but it was not found."
