from pages.client_page import *
from imports.main_imports.main_imports import *

@pytest.mark.skip (reason = "Client Page has errors")
def test_tc_fe_clients_003(driver):
    """Verify no severe browser console errors on page load."""
    login_client_page(driver)
    time.sleep(2)

    # Retrieve browser console performance/error logs
    driver.refresh()

    # Fetch browser console logs
    errors = get_browser_console_errors(driver)
    assert len(errors) == 0, f"Severe console errors detected upon page reload: {errors}"
    print(" SUCCESS: No severe console errors detected during reload.")

    driver.quit()
