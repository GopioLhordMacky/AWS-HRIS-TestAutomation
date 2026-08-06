from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_043(authenticated_driver):
    """Verify the Industry dropdown displays the correct list of options."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open the "Add Client" modal
    TableActions.click_edit_btn_by_row_index(driver, row_idx=1)

    # Expected list of Industry options from test data
    expected_industries = Options.industry_options

    # Step 2: Verify the dropdown options list matches expected options
    assert ComponentVerifier.verify_dropdown_options(
        driver,
        Update_Modal_Inputs.INDUSTRY_SELECT,
        expected_industries
    ), "Industry dropdown options do not match expected list."

    # Step 4: Close the modal using click_close
    ModalActions.click_close(driver)

    driver.quit()