from pages.client_page import *
from imports.main_imports.main_imports import *

@pytest.mark.passed
def test_tc_fe_client_002(driver):
    """Verify Table Headers presence and structure on Client Page."""
    login_client_page(driver)
    time.sleep(1)

    headers = ComponentVerifier.get_table_headers(driver)
    print(f"Captured Headers: {headers}")
    assert len(headers) > 0, "No headers were retrieved from the Client table."
    driver.quit()
