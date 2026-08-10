import time
from utils.navigation_helpers import go_to_client_page


class TestClientPage:

    def test_tc_fe_clients_003(self, authenticated_driver):
        """
        (Functionality) Verify no severe browser console errors on page load.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(2)

        # Checks for errors, prints them if present, and asserts result
        assert page.check_console_error_client(), (
            "Severe console errors detected upon page load."
        )
        print("\nSUCCESS: No severe console errors detected during load.")