from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page


@pytest.mark.passed
def test_tc_fe_clients_008(authenticated_driver):
    """TC_FE_CLIENTS_008: Verify validation when text input fields contain only whitespace."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open Add Client Modal
    ClientPage.click_add_client_button(driver)

    # Step 2: Fill text fields with whitespace and valid dropdowns
    ClientPage.fill_client_form(
        driver,
        contact="   ",
        email="   ",
        phone="   ",
        address="   "
    )

    # Step 3: Click Save
    ModalActions.click_save_only(driver)

    # Step 4: Verify validation message triggers & modal stays open
    assert ComponentVerifier.is_component_visible(
        driver, 
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message failed to appear for whitespace-only input."

    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly."

    driver.quit()