from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from helpers.main_helpers.login import *
from locators.client_page_locators import Login_Locators, Client_Locators
# from data.client_page_inputs import *
from pages.base_page import BasePage
# from pages.client_page import *
# from helpers.main_helpers.check_components import *
# from imports.main_imports.main_imports import *
# from imports.client_page_imports import *

class ClientPage(BasePage):

    # def login_client_page(driver, url="https://test.hris2.awsys-i.com/employee-list", username="macky-temp.gopio@awsys-i.com", password="Awsys123@"):
    #     """Logs in and navigates directly to the Client Page."""
    #     login(driver, username, password, url=url)
    #     navigate_to_page(driver, "Client")

    def is_client_page_loaded(self): # , driver, timeout=10
        """Verifies that the Client page header and table are visible."""
        # wait = WebDriverWait(self.driver, self.timeout)
        try:
            self.wait.until(EC.visibility_of_element_located(Client_Locators.TITLE))
            return True
        except TimeoutException:
            return False

    # def click_add_client_button(driver, timeout=10):
    #     """Clicks the primary Add Client button on the page."""
    #     wait = WebDriverWait(driver, timeout)
    #     btn = wait.until(EC.element_to_be_clickable(Client_Locators.ADD_CLIENT_BUTTON))
    #     btn.click()

    # def click_edit_button(driver, timeout=10):
    #     try:
    #         edit_btn = WebDriverWait(driver, timeout).until(
    #             EC.element_to_be_clickable(Row_Actions.EDIT_BUTTON))
    #         edit_btn.click()
    #         return True
    #     except Exception as e:
    #         print(f"[ERROR] Failed to click Edit button: {e}")
    #         return False
    
    # def get_browser_console_errors(driver):
    #     """Fetches severe browser console log errors."""
    #     logs = driver.get_log("browser")
    #     errors = [entry['message'] for entry in logs if entry['level'] == 'SEVERE']
    #     return errors

    # def select_react_dropdown(driver, locator, option_text):
    #     """Helper to handle React-Select dropdowns by typing and selecting an option.
        
    #     :param locator: Tuple (By, "value") representing the dropdown input element
    #     :param option_text: String text of the option to search and select
    #     """
    #     wait = WebDriverWait(driver, 5)
        
    #     # 1. Accept locator tuple directly instead of forcing By.XPATH
    #     dropdown_input = wait.until(EC.presence_of_element_located(locator))
        
    #     # 2. Clear existing text if any, type target text, and press ENTER
    #     dropdown_input.send_keys(option_text)
    #     time.sleep(2)
    #     dropdown_input.send_keys(Keys.ENTER)

    # def fill_client_form(
    #     driver,
    #     name=ClientFormData.get_unique_client_name(),
    #     industry=ClientFormData.VALID_INDUSTRY,
    #     country=ClientFormData.VALID_COUNTRY,
    #     contact=ClientFormData.VALID_CONTACT_PERSON,
    #     email=ClientFormData.VALID_EMAIL,
    #     phone=ClientFormData.VALID_PHONE,
    #     address=ClientFormData.VALID_ADDRESS
    # ):
    #     """Fills out all fields in the Client modal (Add or Update)."""

    #     wait = WebDriverWait(driver, 10)

    #     # 1. Client Name
    #     name_field = wait.until(EC.element_to_be_clickable(Update_Modal_Inputs.CLIENT_NAME_INPUT))
    #     name_field.clear()
    #     name_field.send_keys(name)

    #     # 2. Dropdowns
    #     if industry:
    #         select_react_dropdown(driver, Update_Modal_Inputs.INDUSTRY_SELECT, industry)
    #         time.sleep(0.5)

    #     if country:
    #         select_react_dropdown(driver, Update_Modal_Inputs.COUNTRY_SELECT, country)
    #         time.sleep(0.5)

    #     # 3. Contact Person
    #     contact_field = driver.find_element(*Update_Modal_Inputs.CONTACT_PERSON_INPUT)
    #     contact_field.clear()
    #     contact_field.send_keys(contact)

    #     # 4. Email
    #     email_field = driver.find_element(*Update_Modal_Inputs.EMAIL_ADDRESS_INPUT)
    #     email_field.clear()
    #     email_field.send_keys(email)

    #     # 5. Phone
    #     phone_field = driver.find_element(*Update_Modal_Inputs.PHONE_NUMBER_INPUT)
    #     phone_field.clear()
    #     phone_field.send_keys(phone)

    #     # 6. Address
    #     address_field = driver.find_element(*Update_Modal_Inputs.ADDRESS_INPUT)
    #     address_field.clear()
    #     address_field.send_keys(address)

    # def update_client_form(
    #     driver,
    #     name=ClientFormData.get_unique_client_name(),
    #     industry=ClientFormData.VALID_INDUSTRY,
    #     country=ClientFormData.VALID_COUNTRY,
    #     contact=ClientFormData.VALID_CONTACT_PERSON,
    #     email=ClientFormData.VALID_EMAIL,
    #     phone=ClientFormData.VALID_PHONE,
    #     address=ClientFormData.VALID_ADDRESS
    # ):
    #     """Fills out all fields in the Client modal (Add or Update)."""

    #     wait = WebDriverWait(driver, 10)

    #     # 1. Client Name
    #     name_field = wait.until(EC.element_to_be_clickable(Update_Modal_Inputs.CLIENT_NAME_INPUT))
    #     name_field.clear()
    #     name_field.send_keys(name)

    #     # 3. Contact Person
    #     contact_field = driver.find_element(*Update_Modal_Inputs.CONTACT_PERSON_INPUT)
    #     contact_field.clear()
    #     contact_field.send_keys(contact)

    #     # 4. Email
    #     email_field = driver.find_element(*Update_Modal_Inputs.EMAIL_ADDRESS_INPUT)
    #     email_field.clear()
    #     email_field.send_keys(email)

    #     # 5. Phone
    #     phone_field = driver.find_element(*Update_Modal_Inputs.PHONE_NUMBER_INPUT)
    #     phone_field.clear()
    #     phone_field.send_keys(phone)

    #     # 6. Address
    #     address_field = driver.find_element(*Update_Modal_Inputs.ADDRESS_INPUT)
    #     address_field.clear()
    #     address_field.send_keys(address)

    #     fill_edit_select_modal(driver, "Country", country)
    #     fill_edit_select_modal(driver, "Industry", industry)


    # def verify_client_modal_fields_are_empty(driver):
    #     """
    #     Verifies that all input fields and textareas in the Client modal are completely empty.

    #     :param driver: WebDriver instance
    #     :return: bool (True if ALL modal fields are empty, False otherwise)
    #     """
    #     fields_to_check = [
    #         ("Client Name", Update_Modal_Inputs.CLIENT_NAME_INPUT),
    #         ("Industry", Update_Modal_Inputs.INDUSTRY_SELECT),
    #         ("Country", Update_Modal_Inputs.COUNTRY_SELECT),
    #         ("Contact Person", Update_Modal_Inputs.CONTACT_PERSON_INPUT),
    #         ("Email Address", Update_Modal_Inputs.EMAIL_ADDRESS_INPUT),
    #         ("Phone Number", Update_Modal_Inputs.PHONE_NUMBER_INPUT),
    #         ("Address", Update_Modal_Inputs.ADDRESS_INPUT),
    #     ]

    #     for field_name, locator in fields_to_check:
    #         if not verify_input_is_empty(driver, locator):
    #             print(f"[Client Modal Check Failed] '{field_name}' field was expected to be empty, but contained data.")
    #             return False

    #     return True