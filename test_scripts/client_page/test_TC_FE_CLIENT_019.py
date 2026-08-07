from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_019(client_page):
    """Verify the Industry dropdown displays the correct list of options."""
    page = client_page


    # Step 1: Open the "Add Client" modal
    page.click_add_client_button()

    # Expected list of Industry options from test data
    expected_industries = Options.industry_options

    # Step 2: Verify the dropdown options list matches expected options
    assert page.verify_dropdown_options(
         
        Update_Modal_Inputs.INDUSTRY_SELECT,
        expected_industries
    ), "Industry dropdown options do not match expected list."

    # Step 3: Select an option ("Automotive") using react dropdown helper
    time.sleep(3)
    page.select_react_dropdown(
         
        Update_Modal_Inputs.INDUSTRY_SELECT,
        "Automotive"
    )

    # Step 4: Close the modal using click_close
    page.click_close()

    