from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_006():
    """TC_FE_CLIENTS_006: Verify UI design and visibility of 'Add Client' modal components."""
    driver = open_browser("chrome")
    login_client_page(driver)
    
    # 1. Click "+ Add Client"
    click_add_client_button(driver)
    
    # 2. Verify Modal Title & Container
    assert is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal body is not visible."
    
    # 3. Verify Form Fields (Inputs & Selects)
    assert is_component_visible(driver, Update_Modal_Inputs.CLIENT_NAME_INPUT), "Client Name input missing."
    assert is_component_visible(driver, Update_Modal_Inputs.INDUSTRY_SELECT), "Industry dropdown missing."
    assert is_component_visible(driver, Update_Modal_Inputs.COUNTRY_SELECT), "Country dropdown missing."
    assert is_component_visible(driver, Update_Modal_Inputs.CONTACT_PERSON_INPUT), "Contact Person input missing."
    assert is_component_visible(driver, Update_Modal_Inputs.EMAIL_ADDRESS_INPUT), "Email Address input missing."
    assert is_component_visible(driver, Update_Modal_Inputs.PHONE_NUMBER_INPUT), "Phone Number input missing."
    assert is_component_visible(driver, Update_Modal_Inputs.ADDRESS_INPUT), "Address input missing."
    
    # 4. Verify Action Buttons
    assert is_component_visible(driver, Modal_Action_Buttons.CLOSE_BUTTON), "Close button missing."
    assert is_component_visible(driver, Modal_Action_Buttons.SAVE_BUTTON), "Save button missing."
    
    close_browser(driver)