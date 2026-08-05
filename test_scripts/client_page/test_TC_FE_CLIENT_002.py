from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_client_002(authenticated_driver):
    """Verify Table Headers presence and structure on Client Page."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    time.sleep(1)

    headers = TableData.get_table_headers(driver)
    print(f"Captured Headers: {headers}")
    assert len(headers) > 0, "No headers were retrieved from the Client table."
    driver.quit()
