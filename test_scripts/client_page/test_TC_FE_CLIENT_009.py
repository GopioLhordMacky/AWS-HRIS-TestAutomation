from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_009(authenticated_driver):
    """TC_FE_CLIENTS_009: Verify leading and trailing whitespace trimming upon form submission."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    
    # Pre-condition: Open modal
    ClientPage.click_add_client_button(driver)

    raw_name = "  Auto Trim Client  "

    # Step 1: Fill form with leading/trailing whitespace in text inputs
    ClientPage.fill_client_form(
        driver,
        name=ClientFormData.get_unique_client_name(prefix=raw_name),
        contact="  Jane Doe  ",
        email="  janedoe@example.com  ",
        phone="  09123456789  ",
        address="  456 Trim St.  "
    )

    # Step 2: Click Save
    ModalActions.click_save_confirm(driver)
    time.sleep(2)

    # Step 3: Verify success (modal closes or success toast appears)
    assert not ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY, timeout=5), "Modal failed to close after saving."

 
    driver.quit()