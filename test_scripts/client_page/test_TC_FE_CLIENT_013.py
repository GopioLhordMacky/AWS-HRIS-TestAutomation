from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_013(self, authenticated_driver):
        """Verify Industry Dropdown Data in Add Client Modal."""
        page = go_to_client_page(authenticated_driver, via="url")


        # Step 1: Open Add Client Modal
        page.click_add_client_button()

        # Steps 2 & 3: Click Industry dropdown and verify options
        assert page.verify_industry_dropdown_options(), "Industry dropdown options do not match expected values."

    