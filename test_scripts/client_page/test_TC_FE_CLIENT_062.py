from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_062(self, authenticated_driver):
        """
        TC_FE_CLIENTS_062: (Functionality) Verify Pagination with single page
        
        1. Filter table using search term "INVALID_!@#123" so that results fit on a single page (0 or 1 page).
        2. Capture initial pagination info string.
        3. Attempt to navigate Next and Previous.
        4. Assert that the pagination text string remains completely unchanged (confirming non-functionality/single-page boundary).
        """
        page = go_to_client_page(authenticated_driver, via="url")


        # Step 1: Perform search to isolate a single page / minimal results
        page.search_in_table_client("INVALID_!@#123")
        time.sleep(2)

        # Step 2: Capture initial pagination text
        initial_pag_info = page.get_pagination_information_client()

        # Step 3: Attempt Next navigation
        try:
            page.go_to_next_page_client()
            time.sleep(1)
        except Exception:
            pass  # Expected if button is disabled or unclickable

        after_next_info = page.get_pagination_information_client()
        assert after_next_info == initial_pag_info, (
            f"Pagination state changed after clicking Next on a single page! "
            f"Expected '{initial_pag_info}', got '{after_next_info}'."
        )

        # Step 4: Attempt Previous navigation
        try:
            page.go_to_prev_page_client()
            time.sleep(1)
        except Exception:
            pass  # Expected if button is disabled or unclickable

        after_prev_info = page.get_pagination_information_client()
        assert after_prev_info == initial_pag_info, (
            f"Pagination state changed after clicking Previous on a single page! "
            f"Expected '{initial_pag_info}', got '{after_prev_info}'."
        )
