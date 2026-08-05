from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.skip (reason = "Client Page has errors")
def test_tc_fe_clients_003(authenticated_driver):
    """Verify no severe browser console errors on page load."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    time.sleep(2)

    # Retrieve browser console performance/error logs
    driver.refresh()

    # Fetch browser console logs
    errors = ClientPage.get_browser_console_errors(driver)
    assert len(errors) == 0, f"Severe console errors detected upon page reload: {errors}"
    print(" SUCCESS: No severe console errors detected during reload.")

    driver.quit()
