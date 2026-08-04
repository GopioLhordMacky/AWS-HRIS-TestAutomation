from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


@pytest.mark.passed
def test_tc_fe_client_001(driver):
    login_client_page(driver)
    time.sleep(2)

    assert ComponentVerifier.is_client_page_loaded(driver), "Client page failed to load header or table."
    driver.quit()

