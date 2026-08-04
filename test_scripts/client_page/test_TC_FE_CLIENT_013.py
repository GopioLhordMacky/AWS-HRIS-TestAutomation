from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_013(driver):
    """Verify Industry Dropdown Data in Add Client Modal."""
    login_client_page(driver)

    # Step 1: Open Add Client Modal
    click_add_client_button(driver)

    # Expected list of options based on requirements
    expected_industry_options = Options.industry_options

    # Steps 2 & 3: Click Industry dropdown and verify options
    assert ComponentVerifier.verify_dropdown_options(
        driver, 
        Update_Modal_Inputs.INDUSTRY_SELECT, 
        expected_industry_options
    ), "Industry dropdown does not contain all expected options or contains invalid data."

    driver.quit()