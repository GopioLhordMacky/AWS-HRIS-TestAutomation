from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_018(driver):
    """Verify 'Add Client' Modal Closes When Clicking Outside of the Modal."""
    login_client_page(driver)

    # Step 1: Open the "Add Client" modal
    click_add_client_button(driver)

    # Fill out the form to test that entered data is not persisted
    fill_client_form(driver)

    # Step 2: Click outside the modal to close it
    ModalActions.click_outside_modal(driver)

    # Verification: Reopen the modal and verify all fields are cleared (data was not saved)
    click_add_client_button(driver)
    assert verify_client_modal_fields_are_empty(driver), "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.CLIENT_NAME) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.INDUSTRY_SELECT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.COUNTRY_SELECT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.CONTACT_PERSON_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.EMAIL_ADDRESS_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted." 

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.PHONE_NUMBER_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert ComponentVerifier.verify_input_is_empty(driver, Update_Modal_Inputs.ADDRESS_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    driver.quit()