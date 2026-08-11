import time
from utils.navigation_helpers import go_to_client_page


class TestClientPage:

    def test_tc_fe_clients_003(self, authenticated_driver):
        """
        (Functionality) Verify no severe browser console errors on page load.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(2)

        is_clean, errors = page.check_console_error_client()

        # Checks for errors, prints them if present, and asserts result
        assert is_clean, f"Console error test failed! Errors found: {errors}"