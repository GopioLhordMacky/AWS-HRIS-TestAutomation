from helpers.client_page_helpers import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *

@pytest.mark.passed
def test_tc_fe_clients_005():
    """TC_FE_CLIENTS_005: Verify the '+ Add Client' button opens the 'Add Client' modal."""
    driver = open_browser("chrome")
    
    # Pre-condition: User already logged in and Clients page is displayed
    login_client_page(driver)
    
    # Step 1: Click the "+ Add Client" button
    click_add_client_button(driver)
    
    # Step 2: Verify the "Add Client" modal pops up using generic component visibility
    assert is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "The 'Add Client' modal failed to pop up."
    
    close_browser(driver)