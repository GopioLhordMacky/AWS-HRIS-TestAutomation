from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_037(self, authenticated_driver):
        """
        (Functionality) Verify Update Action Without Any Changes in the Update Client Modal:
        1. Click the Edit/pencil button.
        2. Verify the "Update Client" modal opens.
        3. Observe input fields and dropdowns without making any changes.
        4. Verify that the Save button is disabled (click_save_only returns False).
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1: Open the modal via edit button
        page.click_edit_btn_by_row_index_client()

        # Step 2 & 3: Assert that Save button cannot be clicked without modifications
        assert not page.is_save_button_clickable_client(), "Save button should be disabled when no changes are made in the modal."
    