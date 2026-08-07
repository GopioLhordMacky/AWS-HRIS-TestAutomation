from utils.navigation_helpers import go_to_client_page

class TestClientPage:

    def test_tc_fe_clients_006(self, authenticated_driver):
        """TC_FE_CLIENTS_006: Verify UI design and visibility of 'Add Client' modal components."""
        page = go_to_client_page (authenticated_driver, via="url")

        # 1. Click "+ Add Client"
        page.click_add_client_button()

        # 2. Verify Modal Title & Container
        assert page.is_client_modal_inputs_visible(), "FAILED"

        # assert page.is_component_visible(  Update_Modal_Inputs.MODAL_BODY), "Modal body is not visible."
        
        # # 3. Verify Form Fields (Inputs & Selects)
        # assert page.is_component_visible(  Update_Modal_Inputs.CLIENT_NAME_INPUT), "Client Name input missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.INDUSTRY_SELECT), "Industry dropdown missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.COUNTRY_SELECT), "Country dropdown missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.CONTACT_PERSON_INPUT), "Contact Person input missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.EMAIL_ADDRESS_INPUT), "Email Address input missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.PHONE_NUMBER_INPUT), "Phone Number input missing."
        # assert page.is_component_visible(  Update_Modal_Inputs.ADDRESS_INPUT), "Address input missing."
        
        # # 4. Verify Action Buttons
        # assert page.is_component_visible(  Modal_Action_Buttons.CLOSE_BUTTON), "Close button missing."
        # assert page.is_component_visible(  Modal_Action_Buttons.SAVE_BUTTON), "Save button missing."
        
