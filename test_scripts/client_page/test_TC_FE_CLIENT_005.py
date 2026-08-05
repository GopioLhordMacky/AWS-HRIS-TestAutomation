from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_005(authenticated_driver):
    """TC_FE_CLIENTS_005: Verify the '+ Add Client' button opens the 'Add Client' modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    time.sleep(1) 
    
    # Step 1: Click the "+ Add Client" button
    ClientPage.click_add_client_button(driver)
    
    # Step 2: Verify the "Add Client" modal pops up using generic component visibility
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "The 'Add Client' modal failed to pop up."
    
    driver.quit()