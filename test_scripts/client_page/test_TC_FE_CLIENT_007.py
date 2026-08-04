from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_007(driver):
    """TC_FE_CLIENTS_007: Verify required input validation on empty form submission."""
    login_client_page(driver)
    
    # Pre-condition: Open Add Client Modal
    click_add_client_button(driver)
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal failed to display."
    
    # Step 1: Click Save with all required fields left blank
    driver.find_element(*Modal_Action_Buttons.SAVE_BUTTON).click()
    
    # Step 2: Verify validation message pops up
    assert ComponentVerifier.is_component_visible(
        driver, 
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message 'Client Name is required!' failed to display."
    
    # Step 3: Verify modal remains open and does not save/close
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly after invalid submission."
    
    driver.close()