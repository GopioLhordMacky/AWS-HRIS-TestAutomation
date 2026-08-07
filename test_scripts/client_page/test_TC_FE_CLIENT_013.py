from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_013(client_page):
    """Verify Industry Dropdown Data in Add Client Modal."""
    page = client_page


    # Step 1: Open Add Client Modal
    page.click_add_client_button()

    # Expected list of options based on requirements
    expected_industry_options = Options.industry_options

    # Steps 2 & 3: Click Industry dropdown and verify options
    assert page.verify_dropdown_options(
          
        Update_Modal_Inputs.INDUSTRY_SELECT, 
        expected_industry_options
    ), "Industry dropdown does not contain all expected options or contains invalid data."

    