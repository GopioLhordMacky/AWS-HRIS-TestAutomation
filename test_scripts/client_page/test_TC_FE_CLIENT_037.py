from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
# from locators.shared.shared_locators import Modal_Locators

@pytest.mark.passed
def test_tc_fe_clients_037():
    """
    (Functionality) Verify Update Action Without Any Changes in the Update Client Modal:
    1. Click the Edit/pencil button.
    2. Verify the "Update Client" modal opens.
    3. Observe input fields and dropdowns without making any changes.
    4. Verify that the Save button is disabled (click_save_only returns False).
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open the modal via edit button
    assert click_edit_button(driver), "Failed to click the Edit button!"

    # Step 2 & 3: Assert that Save button cannot be clicked without modifications
    assert not  is_component_clickable(driver, ModalLocators.SAVE_BUTTON, timeout=5), "Save button was clickable/enabled even though no changes were made in the Update Client modal!"

    close_browser(driver)