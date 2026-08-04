from helpers.client_page_helpers import *
from imports.main_imports.main_imports import *


class TestClient002:

    @pytest.mark.passed
    def test_tc_fe_client_002(self):
        """Verify Table Headers presence and structure on Client Page."""
        driver = open_browser("chrome")
        login_client_page(driver)
        time.sleep(1)

        headers = get_table_headers(driver)
        print(f"Captured Headers: {headers}")
        assert len(headers) > 0, "No headers were retrieved from the Client table."
        close_browser(driver)

if __name__ == "__main__":
    TestClient002().test_tc_fe_client_002()