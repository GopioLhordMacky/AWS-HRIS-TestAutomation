from utils.navigation_helpers import go_to_client_page
import time

def test_navigate_to_client_page_via_sidebar(authenticated_driver):

    client_page = go_to_client_page(authenticated_driver, via="url")

    assert client_page.is_client_page_loaded(), "Failed to load Client Page via sidebar navigation."

    time.sleep(5)  # Optional: For visual confirmation during test runs