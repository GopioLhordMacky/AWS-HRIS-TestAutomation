from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_013(authenticated_driver):
    """Verify Industry Dropdown Data in Add Client Modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open Add Client Modal
    ClientPage.click_add_client_button(driver)

    # Expected list of options based on requirements
    expected_industry_options = Options.industry_options

    # Steps 2 & 3: Click Industry dropdown and verify options
    assert ComponentVerifier.verify_dropdown_options(
        driver, 
        Update_Modal_Inputs.INDUSTRY_SELECT, 
        expected_industry_options
    ), "Industry dropdown does not contain all expected options or contains invalid data."

    driver.quit()