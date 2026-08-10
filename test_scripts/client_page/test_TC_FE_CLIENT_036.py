from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

class TestClientPage:
    def test_tc_fe_clients_036(self, authenticated_driver):
        """TC_FE_CLIENTS_010: Verify Dropdown Loading Performance in '+ Add Client' Modal."""
        page = go_to_client_page(authenticated_driver, via="url")
        
        # Step 1: Open Add Client Modal
        page.click_edit_btn_by_row_index_client()  # Assuming the first row is used for testing
        assert page.is_client_modal_visible_client(), "Expected 'Add Client' modal to be visible after clicking the Edit button, but it was not found."

        # Step 2: Measure Industry Dropdown Performance
        start_time = time.perf_counter()
        page.fill_industry_select_modal_client()
        industry_duration = time.perf_counter() - start_time

        assert industry_duration < 3.0, f"Industry dropdown selection took too long: {industry_duration:.2f}s"

        # Step 3: Measure Country Dropdown Performance
        start_time = time.perf_counter()
        page.fill_country_select_modal_client()
        country_duration = time.perf_counter() - start_time

        assert country_duration < 3.0, f"Country dropdown selection took too long: {country_duration:.2f}s"

    