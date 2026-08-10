
from data.client_page_inputs import ClientFormData
from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_010(self, authenticated_driver):
        """TC_FE_CLIENTS_010: Verify Dropdown Loading Performance in '+ Add Client' Modal."""
        page = go_to_client_page(authenticated_driver, via="url")


        # Step 1: Open Add Client Modal
        assert page.click_add_client_button(), "Failed to click the '+ Add Client' button."
        assert page.is_client_modal_visible(), "The 'Add Client' modal failed to pop up."

        # Step 2: Measure Industry Dropdown Performance
        start_time = time.perf_counter()
        assert page.fill_industry_select_modal_client(), "Failed to fill industry dropdown."
        industry_duration = time.perf_counter() - start_time

        assert industry_duration < 3.0, f"Industry dropdown selection took too long: {industry_duration:.2f}s"

        # Step 3: Measure Country Dropdown Performance
        start_time = time.perf_counter()
        assert page.fill_country_select_modal_client(), "Failed to fill country dropdown."
        country_duration = time.perf_counter() - start_time

        assert country_duration < 3.0, f"Country dropdown selection took too long: {country_duration:.2f}s"

    