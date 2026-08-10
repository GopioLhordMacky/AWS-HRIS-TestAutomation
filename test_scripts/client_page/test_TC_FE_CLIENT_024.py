from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_024(self, authenticated_driver):
        """
        (Functionality) Verify Default Selected Value in Status Dropdown:
        1. The default selected value should be Active.
        2. The dropdown should not have a null or empty value selected by default.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        # Step 1 & 2: Verify default value is 'Active' and neither empty nor null
        assert page.verify_status_input_matches_client(), f"Expected Status dropdown options not found mismatching options."
