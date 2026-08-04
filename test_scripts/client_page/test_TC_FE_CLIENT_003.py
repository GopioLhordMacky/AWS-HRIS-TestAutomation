from helpers.client_page_helpers import *
from imports.main_imports.main_imports import *

class TestClient003:

    @pytest.mark.skip (reason = "Client Page has errors")
    def test_tc_fe_clients_003(self):
        """Verify no severe browser console errors on page load."""
        driver = open_browser("chrome")
        login_client_page(driver)
        time.sleep(2)

        # Retrieve browser console performance/error logs
        driver.refresh()

        # Fetch browser console logs
        errors = get_browser_console_errors(driver)
        assert len(errors) == 0, f"Severe console errors detected upon page reload: {errors}"
        print(" SUCCESS: No severe console errors detected during reload.")

        close_browser(driver)

if __name__ == "__main__":
    TestClient003().test_tc_fe_clients_003()