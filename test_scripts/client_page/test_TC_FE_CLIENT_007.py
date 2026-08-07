from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_clients_007(client_page):
    """TC_FE_CLIENTS_007: Verify required input validation on empty form submission."""
    page = client_page

    # Pre-condition: Open Add Client Modal
    page.click_add_client_button()
    assert page.is_component_visible(  Update_Modal_Inputs.MODAL_BODY), "Modal failed to display."
    
    # Step 1: Click Save with all required fields left blank
    page.click_save_only()
    
    # Step 2: Verify validation message pops up
    assert page.is_component_visible(
          
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message 'Client Name is required!' failed to display."
    
    # Step 3: Verify modal remains open and does not save/close
    assert page.is_component_visible(  Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly after invalid submission."
    
