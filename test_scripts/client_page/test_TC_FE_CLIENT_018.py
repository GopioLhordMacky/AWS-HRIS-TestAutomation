from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_018(client_page):
    """Verify 'Add Client' Modal Closes When Clicking Outside of the Modal."""
    page = client_page


    # Step 1: Open the "Add Client" modal
    page.click_add_client_button()
    
    # Fill out the form to test that entered data is not persisted
    page.fill_client_form()

    # Step 2: Click outside the modal to close it
    page.click_outside_modal()

    # Verification: Reopen the modal and verify all fields are cleared (data was not saved)
    page.click_add_client_button()
    assert page.verify_client_modal_fields_are_empty(), "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.CLIENT_NAME) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.INDUSTRY_SELECT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.COUNTRY_SELECT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.CONTACT_PERSON_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.EMAIL_ADDRESS_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted." 

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.PHONE_NUMBER_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    # assert page.verify_input_is_empty(  Update_Modal_Inputs.ADDRESS_INPUT) , \
    #     "Expected modal fields to be empty/cleared after closing via outside click, but data persisted."

    