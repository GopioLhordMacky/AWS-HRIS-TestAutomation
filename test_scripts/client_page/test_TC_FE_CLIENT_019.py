from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_019(driver):
    """Verify the Industry dropdown displays the correct list of options."""
    login_client_page(driver)

    # Step 1: Open the "Add Client" modal
    click_add_client_button(driver)

    # Expected list of Industry options from test data
    expected_industries = Options.industry_options

    # Step 2: Verify the dropdown options list matches expected options
    assert ComponentVerifier.verify_dropdown_options(
        driver,
        Update_Modal_Inputs.INDUSTRY_SELECT,
        expected_industries
    ), "Industry dropdown options do not match expected list."

    # Step 3: Select an option ("Automotive") using react dropdown helper
    time.sleep(3)
    select_react_dropdown(
        driver,
        Update_Modal_Inputs.INDUSTRY_SELECT,
        "Automotive"
    )

    # Step 4: Close the modal using click_close
    ModalActions.click_close(driver)

    driver.quit()