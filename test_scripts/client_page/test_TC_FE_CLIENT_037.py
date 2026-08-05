from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_037(authenticated_driver):
    """
    (Functionality) Verify Update Action Without Any Changes in the Update Client Modal:
    1. Click the Edit/pencil button.
    2. Verify the "Update Client" modal opens.
    3. Observe input fields and dropdowns without making any changes.
    4. Verify that the Save button is disabled (click_save_only returns False).
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open the modal via edit button
    assert ClientPage.click_edit_button(driver), "Failed to click the Edit button!"

    # Step 2 & 3: Assert that Save button cannot be clicked without modifications
    assert not  ComponentVerifier.is_component_clickable(driver, ModalLocators.SAVE_BUTTON, timeout=5), "Save button was clickable/enabled even though no changes were made in the Update Client modal!"

    driver.quit()