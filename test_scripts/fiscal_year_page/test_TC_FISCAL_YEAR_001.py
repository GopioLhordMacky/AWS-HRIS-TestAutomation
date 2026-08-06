from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_fiscal_year_page


@pytest.mark.passed
def test_tc_fe_client_001(authenticated_driver):
    driver = authenticated_driver
    go_to_fiscal_year_page(driver, via="url")
    time.sleep(2)

    driver.quit()


