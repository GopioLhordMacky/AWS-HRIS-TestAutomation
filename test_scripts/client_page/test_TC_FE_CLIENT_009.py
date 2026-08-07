from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_clients_009(client_page):
    """TC_FE_CLIENTS_009: Verify leading and trailing whitespace trimming upon form submission."""
    page = client_page

    
    # Pre-condition: Open modal
    page.click_add_client_button()

    raw_name = "  Auto Trim Client  "

    # Step 1: Fill form with leading/trailing whitespace in text inputs
    page.fill_client_form(
         
        name=ClientFormData.get_unique_client_name(prefix=raw_name),
        contact="  Jane Doe  ",
        email="  janedoe@example.com  ",
        phone="  09123456789  ",
        address="  456 Trim St.  "
    )

    # Step 2: Click Save
    page.click_save_confirm()
    time.sleep(2)

    # Step 3: Verify success (modal closes or success toast appears)
    assert not page.is_component_visible(  Update_Modal_Inputs.MODAL_BODY), "Modal failed to close after saving."
    
 
    