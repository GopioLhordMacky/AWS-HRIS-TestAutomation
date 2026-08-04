from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_043():
    """Verify the Industry dropdown displays the correct list of options."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open the "Add Client" modal
    click_edit_btn_by_row_index(driver, row_idx=1)

    # Expected list of Industry options from test data
    expected_industries = Options.industry_options

    # Step 2: Verify the dropdown options list matches expected options
    assert verify_dropdown_options(
        driver,
        Update_Modal_Inputs.INDUSTRY_SELECT,
        expected_industries
    ), "Industry dropdown options do not match expected list."

    # Step 4: Close the modal using click_close
    click_close(driver)

    close_browser(driver)