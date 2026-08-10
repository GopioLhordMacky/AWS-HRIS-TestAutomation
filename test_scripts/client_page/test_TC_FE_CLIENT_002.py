import time
from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_client_002(self, authenticated_driver):
        """Verify Table Headers presence and structure on Client Page."""
        page = go_to_client_page(authenticated_driver, via="url")
        time.sleep(1)

        headers = page.get_table_headers_client()
        print(f"Captured Headers: {headers}")
        assert len(headers) > 0, "No headers were retrieved from the Client table."
        
