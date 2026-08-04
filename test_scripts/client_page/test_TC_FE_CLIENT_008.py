from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *


@pytest.mark.passed
def test_tc_fe_clients_008(driver):
    """TC_FE_CLIENTS_008: Verify validation when text input fields contain only whitespace."""
    login_client_page(driver)

    # Step 1: Open Add Client Modal
    click_add_client_button(driver)

    # Step 2: Fill text fields with whitespace and valid dropdowns
    fill_client_form(
        driver,
        contact="   ",
        email="   ",
        phone="   ",
        address="   "
    )

    # Step 3: Click Save
    driver.find_element(*Modal_Action_Buttons.SAVE_BUTTON).click()

    # Step 4: Verify validation message triggers & modal stays open
    assert ComponentVerifier.is_component_visible(
        driver, 
        Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
    ), "Validation message failed to appear for whitespace-only input."

    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal closed unexpectedly."

    driver.quit()