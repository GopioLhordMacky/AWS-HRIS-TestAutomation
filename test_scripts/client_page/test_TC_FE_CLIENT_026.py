from utils.navigation_helpers import go_to_client_page


class TestClientPage:
    def test_tc_fe_clients_026(self, authenticated_driver):
        """
        (Accessibility) Verify that Status dropdown can be navigated 
        and activated using keyboard.
        1. Focus Status dropdown via keyboard navigation.
        2. Press keys (Arrow Down, Enter) to select 'Inactive'.
        3. Verify that selected option updates correctly and reflects in table toggles.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1-4: Focus Status dropdown, navigate down to 'Inactive', and press ENTER
        target_status = "Inactive"

        page.tab_navigation_status_filter()

        # Step 5: Verify table updates to display 'Inactive' toggles
        assert page.check_toggle_status_on_table_client(
            column_name="Active",
            text=target_status
        ), f"Keyboard selection failed! Table did not update to reflect '{target_status}' records."
