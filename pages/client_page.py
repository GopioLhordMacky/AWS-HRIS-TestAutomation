from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.client_page_locators import *
from data.client_page_inputs import *
from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from pages.base_page import BasePage
from components.tables import Table
from components.elements import Element

class ClientPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver) 
        self.table = Table(driver)   
        self.element = Element(driver)           
        self.navigation = Navigation(driver)

    def click_add_client_button(self):
        """Clicks the primary Add Client button on the page."""
        self.wait_for_and_click(Client_Locators.ADD_CLIENT_BUTTON)

    def click_edit_button(self):
        """Clicks the Edit button for a row item."""
        try:
            self.wait_for_and_click(Row_Actions.EDIT_BUTTON)
            return True
        except Exception as e:
            print(f"[ERROR] Failed to click Edit button: {e}")
            return False

    def is_client_modal_inputs_visible(self):
        return all ([
            self.element.is_component_visible(Update_Modal_Inputs.CLIENT_NAME_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.INDUSTRY_SELECT),
            self.element.is_component_visible(Update_Modal_Inputs.COUNTRY_SELECT),
            self.element.is_component_visible(Update_Modal_Inputs.CONTACT_PERSON_INPUT)
        ])
       

    def is_client_modal_visible(self):
        return self.element.is_component_visible(Update_Modal_Inputs.MODAL_BODY)
    
    def get_table_headers_client(self):
        return self.table.get_table_headers()

    def ensure_element_visible(self, locator):
        """
        Waits until an element is visible in the DOM and returns it.
        Uses the instance's standard explicit wait engine (self.wait).

        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_react_dropdown(self, locator, option_text):
        """
        Handles React-Select and modern custom dropdowns by typing and selecting an option.
        
        :param locator: Tuple (By, value) representing the dropdown input element
        :param option_text: String text of the option to search and select
        """
        try:
            # 1. Wait until the input element is ready to accept interaction
            dropdown_input = self.wait.until(EC.element_to_be_clickable(locator))
            
            # 2. Click to open/focus, clear existing text, and type search string
            dropdown_input.click()
            dropdown_input.send_keys(Keys.CONTROL + "a")
            dropdown_input.send_keys(Keys.BACKSPACE)
            dropdown_input.send_keys(option_text)
            
            # 3. Wait for option container or menu item to appear, then select
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{option_text}')]"))
            )
            dropdown_input.send_keys(Keys.ENTER)
            
        except TimeoutException:
            print(f"Failed to locate or select option '{option_text}' in React dropdown {locator}")
            raise

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

        self.fill_edit_select_modal("Country", country)
        self.fill_edit_select_modal("Industry", industry)

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