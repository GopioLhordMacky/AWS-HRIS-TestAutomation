from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.client_page_locators import *
from data.client_page_inputs import *
from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from pages.base_page import BasePage

class ClientPage(
    TableData, 
    TableActions, 
    TableSearch, 
    TablePagination, 
    ComponentVerifier, 
    FormControls, 
    ModalActions,
    BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_client_button(self, timeout=10):
        """Clicks the primary Add Client button on the page."""
        self.wait_for_and_click(Client_Locators.ADD_CLIENT_BUTTON, timeout=timeout)

    def click_edit_button(self, timeout=10):
        """Clicks the Edit button for a row item."""
        try:
            self.wait_for_and_click(Row_Actions.EDIT_BUTTON, timeout=timeout)
            return True
        except Exception as e:
            print(f"[ERROR] Failed to click Edit button: {e}")
            return False

    def fill_client_form(
        self,
        name=None,
        industry=ClientFormData.VALID_INDUSTRY,
        country=ClientFormData.VALID_COUNTRY,
        contact=ClientFormData.VALID_CONTACT_PERSON,
        email=ClientFormData.VALID_EMAIL,
        phone=ClientFormData.VALID_PHONE,
        address=ClientFormData.VALID_ADDRESS
    ):
        """Fills out all fields in the Client modal (Add)."""
        # Resolve dynamic default values at runtime
        name = name if name is not None else ClientFormData.get_unique_client_name()

        # 1. Client Name
        self.wait_and_type(Update_Modal_Inputs.CLIENT_NAME_INPUT, name)

        # 2. Dropdowns (Uses BasePage select method)
        if industry:
            self.select_react_dropdown(Update_Modal_Inputs.INDUSTRY_SELECT, industry)
            time.sleep(0.5)

        if country:
            self.select_react_dropdown(Update_Modal_Inputs.COUNTRY_SELECT, country)
            time.sleep(0.5)

        # 3. Text Inputs
        self.wait_and_type(Update_Modal_Inputs.CONTACT_PERSON_INPUT, contact)
        self.wait_and_type(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT, email)
        self.wait_and_type(Update_Modal_Inputs.PHONE_NUMBER_INPUT, phone)
        self.wait_and_type(Update_Modal_Inputs.ADDRESS_INPUT, address)

    def update_client_form(
        self,
        name=None,
        industry=ClientFormData.VALID_INDUSTRY,
        country=ClientFormData.VALID_COUNTRY,
        contact=ClientFormData.VALID_CONTACT_PERSON,
        email=ClientFormData.VALID_EMAIL,
        phone=ClientFormData.VALID_PHONE,
        address=ClientFormData.VALID_ADDRESS
    ):
        """Fills out fields in the Client modal (Update)."""
        name = name if name is not None else ClientFormData.get_unique_client_name()

        self.wait_and_type(Update_Modal_Inputs.CLIENT_NAME_INPUT, name)
        self.wait_and_type(Update_Modal_Inputs.CONTACT_PERSON_INPUT, contact)
        self.wait_and_type(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT, email)
        self.wait_and_type(Update_Modal_Inputs.PHONE_NUMBER_INPUT, phone)
        self.wait_and_type(Update_Modal_Inputs.ADDRESS_INPUT, address)

        ModalActions.fill_edit_select_modal(self.driver, "Country", country)
        ModalActions.fill_edit_select_modal(self.driver, "Industry", industry)

    def verify_client_modal_fields_are_empty(self):
        """
        Verifies that all input fields and textareas in the Client modal are completely empty.

        :return: bool (True if ALL modal fields are empty, False otherwise)
        """
        fields_to_check = [
            ("Client Name", Update_Modal_Inputs.CLIENT_NAME_INPUT),
            ("Industry", Update_Modal_Inputs.INDUSTRY_SELECT),
            ("Country", Update_Modal_Inputs.COUNTRY_SELECT),
            ("Contact Person", Update_Modal_Inputs.CONTACT_PERSON_INPUT),
            ("Email Address", Update_Modal_Inputs.EMAIL_ADDRESS_INPUT),
            ("Phone Number", Update_Modal_Inputs.PHONE_NUMBER_INPUT),
            ("Address", Update_Modal_Inputs.ADDRESS_INPUT),
        ]

        for field_name, locator in fields_to_check:
            if not self.verify_input_is_empty(locator):
                print(f"[Client Modal Check Failed] '{field_name}' field was expected to be empty, but contained data.")
                return False

        return True