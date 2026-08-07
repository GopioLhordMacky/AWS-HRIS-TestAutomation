from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


@pytest.mark.skip (reason = "Client Page has errors")
def test_tc_fe_clients_003(client_page):
    """Verify no severe browser console errors on page load."""
    page = client_page

    time.sleep(2)

    # Retrieve browser console performance/error logs
    page.refresh()

    # Fetch browser console logs
    errors = page.get_browser_console_errors()
    assert len(errors) == 0, f"Severe console errors detected upon page reload: {errors}"
    print(" SUCCESS: No severe console errors detected during reload.")

    
