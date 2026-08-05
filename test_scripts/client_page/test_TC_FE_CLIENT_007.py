from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_007(authenticated_driver):
    """TC_FE_CLIENTS_007: Verify required input validation on empty form submission."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    
    # Pre-condition: Open Add Client Modal
    ClientPage.click_add_client_button(driver)
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal failed to display."
    
    # Step 1: Click Save with all required fields left blank
    ModalActions.click_save_only(driver)
    
    # Step 2: Verify validation message pops up
    assert ComponentVerifier.is_component_visible(
        driver, 
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message 'Client Name is required!' failed to display."
    
    # Step 3: Verify modal remains open and does not save/close
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly after invalid submission."
    
    driver.close()