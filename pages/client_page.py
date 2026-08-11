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
from components.modals import Modals

class ClientPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver) 
        self.table = Table(driver)   
        self.element = Element(driver)           
        self.navigation = Navigation(driver)
        self.modal = Modals(driver)
# =========================================================================
    # PAGE LEVEL ACTIONS
    # =========================================================================

    def check_console_error_client(self):
        """Checks browser console for errors."""
        return self.get_browser_console_errors()
       

    def click_add_client_button(self):
        """Clicks the primary Add Client button on the page."""
        self.wait_for_and_click(Client_Locators.ADD_CLIENT_BUTTON)
        return self  # Return self for method chaining

    def click_edit_button_client(self):
        """Clicks the Edit button for a row item."""
        try:
            self.wait_for_and_click(Row_Actions.EDIT_BUTTON)
            return True
        except Exception as e:
            print(f"[ERROR] Failed to click Edit button: {e}")
            return False

# =========================================================================
    # VISIBILITY & STATUS CHECKS (ELEMENT COMPONENT DELEGATION)
    # =========================================================================

    def find_next_button(self):
        return self.find_element(PaginationLocators.NEXT_PAGE_BTN)

    def find_prev_button(self):
        return self.find_element(PaginationLocators.PREV_PAGE_BTN)

    def is_row_per_page_dropdown_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.ROWS_PER_PAGE_DROPDOWN)

    def is_next_page_button_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.NEXT_PAGE_BTN)

    def is_next_prev_button_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.PREV_PAGE_BTN)

    def is_confirm_button_visible(self):
        return self.element.is_component_visible(ModalLocators.CONFIRM_BUTTON)

    def is_cancel_button_visible(self):
        return self.element.is_component_visible(ModalLocators.CANCEL_BUTTON)
    
    def is_save_button_clickable_client(self):
        """Checks if the Save button in the modal is clickable."""
        return self.element.is_component_clickable(ModalLocators.SAVE_BUTTON)

    def is_close_button_clickable_client(self):
        """Checks if the Close button in the modal is clickable."""
        return self.element.is_component_clickable(ModalLocators.CLOSE_BUTTON)
    
    def is_client_modal_inputs_visible_client(self):
        """Verifies if all core input fields inside the client modal are visible."""
        return all([
            self.element.is_component_visible(Update_Modal_Inputs.CLIENT_NAME_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.INDUSTRY_SELECT),
            self.element.is_component_visible(Update_Modal_Inputs.COUNTRY_SELECT),
            self.element.is_component_visible(Update_Modal_Inputs.CONTACT_PERSON_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.PHONE_NUMBER_INPUT),
        ])

    def is_client_modal_buttons_visible_client(self):
        """Verifies if the action buttons inside the client modal are visible."""
        return all([
            self.element.is_component_visible(Modal_Action_Buttons.CLOSE_BUTTON),
            self.element.is_component_visible(Modal_Action_Buttons.SAVE_BUTTON)
        ])

    def is_client_modal_visible_client(self):
        """Verifies if the main modal body is visible."""
        return self.element.is_component_visible(Update_Modal_Inputs.MODAL_BODY)

    def is_toast_notification_visible_client(self):
        """Verifies if the error validation toast message is visible."""
        return self.element.is_component_visible(
            Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE
        )

    def is_add_client_button_visible_client(self):
        """Verifies if the Add Client button is visible on the page."""
        return self.element.is_component_visible(Client_Locators.ADD_CLIENT_BUTTON)

    def is_search_bar_and_dropdown_visible_client(self):
        """Verifies if search and filter dropdown controls are visible."""
        return all([
            self.element.is_component_visible(Filter_and_Search_Section.SEARCH_BAR),
            self.element.is_component_visible(Filter_and_Search_Section.STATUS_FILTER_DROPDOWN),
            self.element.is_component_visible(Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN)
        ])

    def is_pagination_component_visible_client(self):
        """Verifies if the table pagination container is visible."""
        return self.element.is_component_visible(Pagination_Section.PAGINATION_CONTAINER)

    def verify_country_dropdown_options(self, 
                                        dropdown_locator = Update_Modal_Inputs.COUNTRY_SELECT,
                                        expected_options = Options.country_options,
                                        options_locator=None):
        """Verifies dropdown options against expected list."""
        return self.element.verify_dropdown_options(dropdown_locator, expected_options, options_locator)

    def verify_industry_dropdown_options(self, 
                                        dropdown_locator = Update_Modal_Inputs.INDUSTRY_SELECT,
                                        expected_options = Options.industry_options,
                                        options_locator=None):
        """Verifies dropdown options against expected list."""
        return self.element.verify_dropdown_options(dropdown_locator, expected_options, options_locator)

    def verify_status_dropdown_options(self, 
                                    dropdown_locator = Filter_and_Search_Section.STATUS_FILTER_DROPDOWN,
                                    expected_options = Options.status_options,
                                    options_locator=None):
        """Verifies dropdown options against expected list."""
        return self.element.verify_dropdown_options(dropdown_locator, expected_options, options_locator)

    def verify_input_is_empty_client(self, locator):
        """Verifies whether an input field is empty."""
        return self.element.verify_input_is_empty(locator)

    def verify_search_input_matches_client(self, locator= Filter_and_Search_Section.SEARCH_BAR, expected_text=None):
        """Verifies if an input value matches expected text."""
        return self.element.verify_input_matches(locator, expected_text)

    def verify_industry_input_matches_client(self, locator= Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN, expected_text=None):
        """Verifies if an input value matches expected text."""
        return self.element.verify_input_matches(locator, expected_text)

    def verify_status_input_matches_client(self, locator= Filter_and_Search_Section.STATUS_FILTER_DROPDOWN, expected_text="Active"):
        """Verifies if an input value matches expected text."""
        return self.element.verify_input_matches(locator, expected_text)

    def select_industry_filter_client(self, option_text):
        """Selects an option from a labeled custom dropdown."""
        return self.element.select_custom_dropdown("Industry", option_text)

    def select_status_filter_client(self, option_text):
        """Selects an option from a labeled custom dropdown."""
        return self.element.select_custom_dropdown("Status", option_text)

    def toggle_active_status_client(self, row_index, column_name="Active"):
        """Toggles active switch in a specific table row."""
        return self.element.toggle_active_status(row_index, column_name)

    def verify_active_toggle_state_client(self, row_index, column_name="Active"):
        """Checks if active status toggle is selected."""
        return self.element.verify_active_toggle_state(row_index, column_name)

# =========================================================================
    # MODAL UTILITIES (MODALS COMPONENT DELEGATION)
    # =========================================================================
    def click_close_modal_client(self):
        """Clicks close button in modal."""
        self.modal.click_close()
        return True and self

    def click_confirm_modal_client(self):
        """Clicks confirm button in modal dialog."""
        self.modal.click_confirm()
        return self

    def click_cancel_modal_client(self):
        """Clicks cancel button in modal."""
        self.modal.click_cancel()
        return True and self

    def click_save_only_modal_client(self):
        """Clicks save button in modal."""
        self.modal.click_save_only()
        return True and self

    def click_save_confirm_modal_client(self):
        """Clicks save and then secondary confirm button."""
        self.modal.click_save_confirm()
        return self

    def click_close_x_modal_client(self):
        """Clicks header X button on modal."""
        self.modal.click_close_x()
        return self

    def click_outside_modal_client(self):
        """Dismisses modal by hitting ESC."""
        self.modal.click_outside_modal()
        return self

    def fill_edit_text_modal_client(self, field_identifier, new_text):
        """Clears and fills input field inside a modal."""
        self.modal.fill_edit_text_modal(field_identifier, new_text)
        return self

    def fill_industry_select_modal_client(self, new_option = ClientFormData.VALID_INDUSTRY):
        """Clears and selects option inside modal dropdown."""
        self.modal.fill_edit_select_modal("Industry", new_option)
        return self

    def fill_country_select_modal_client(self, new_option = ClientFormData.VALID_COUNTRY):
        """Clears and selects option inside modal dropdown."""
        self.modal.fill_edit_select_modal("Country", new_option)
        return self

    def check_error_message_client(self, expected_text=None):
        """Verifies inline/modal error messages."""
        return True and self.modal.check_error_message(expected_text)

    def check_toast_message_client(self, expected_text=None):
        """Verifies toast popup message."""
        return self.modal.check_toast_message(expected_text)

# =========================================================================
    # NAVIGATION UTILITIES (NAVIGATION COMPONENT DELEGATION)
    # =========================================================================

    def navigate_to_page(self, client_page):
        """Navigates to a specific sidebar page."""
        self.navigation.navigate_to_page(client_page)
        return True and self

    def switch_tab_client(self, tab_name):
        """Switches sub-tabs on client page."""
        return self.navigation.switch_tab(tab_name)

    def switch_view_mode_client(self, mode="table"):
        """Toggles table vs card view mode."""
        return self.navigation.switch_view_mode(mode)

    def tab_navigation_client(self, locator, keys=None, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(locator, keys, helper, *helper_args, **helper_kwargs)

    def tab_navigation_industry_filter(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
                                               [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER],
                                                 helper, *helper_args, **helper_kwargs)

    def tab_navigation_status_filter(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Filter_and_Search_Section.STATUS_FILTER_DROPDOWN,
                                                [Keys.ARROW_DOWN, Keys.ENTER],
                                                    helper, *helper_args, **helper_kwargs)

    def tab_navigation_toggle_status(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Row_Actions.ACTIVE_TOGGLE,
                                                [Keys.SPACE],
                                                    helper, *helper_args, **helper_kwargs)

    def tab_navigation_search_bar(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Filter_and_Search_Section.SEARCH_BAR,
                                                [Keys.ENTER],
                                                    helper, *helper_args, **helper_kwargs)

    def tab_navigation_next_btn(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(PaginationLocators.NEXT_PAGE_BTN,
                                                [Keys.ENTER],
                                                        helper, *helper_args, **helper_kwargs)

    def tab_navigation_prev_btn(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(PaginationLocators.PREV_PAGE_BTN,
                                                [Keys.SPACE],
                                                        helper, *helper_args, **helper_kwargs)

    # =========================================================================
    # TABLE UTILITIES (TABLE COMPONENT DELEGATION)
    # =========================================================================
    def get_dropdown_value(self, label_name):
        xpath = (
            f"//div[contains(@class, 'modal-content')]"
            f"//label[normalize-space()='{label_name}']"
            f"/following::div[contains(@class, 'singleValue') or contains(@class, '-singleValue')][1]"
        )
        # Since find_elements returns a single WebElement (or None):
        elem = self.find_elements(By.XPATH, xpath)
        return elem.text.strip() if elem else ""
        
    def get_client_name(self):
            """Retrieves value text from Client Name input field."""
            try:
                elem = self.find_element(Update_Modal_Inputs.CLIENT_NAME_INPUT)
                # If elem is a WebElement instance, fetch value attribute
                val = elem.get_attribute("value")
                return val.strip() if val else ""
            except Exception as e:
                print(f"[ERROR] Failed to get client name: {e}")
                return ""

    def get_contact_person(self):
        """Retrieves value text from Contact Person input field."""
        try:
            elem = self.find_element(Update_Modal_Inputs.CONTACT_PERSON_INPUT)
            val = elem.get_attribute("value")
            return val.strip() if val else ""
        except Exception as e:
            print(f"[ERROR] Failed to get contact person: {e}")
            return ""

    def get_table_headers_client(self):
        """Retrieves list of table header titles."""
        return self.table.get_table_headers()

    def get_table_cell_value_client(self, column_name: str, row_idx: int = 1) -> str:
        """Retrieves cell value by column name and row index."""
        return self.table.get_table_cell_value(column_name=column_name, row_idx=row_idx)

    def get_initial_client_name(self, row_idx: int = 1) -> str:
        return self.get_table_cell_value_client("Client Name", row_idx)

    def get_initial_industry(self, row_idx: int = 1) -> str:
        return self.get_table_cell_value_client("Industry", row_idx)

    def get_initial_country(self, row_idx: int = 1) -> str:
        return self.get_table_cell_value_client("Country", row_idx)

    def get_initial_contact_person(self, row_idx: int = 1) -> str:
        return self.get_table_cell_value_client("Contact Person", row_idx)
    def count_table_rows_client(self):
        """Returns count of visible rows in table."""
        return self.table.count_table_rows()

    def get_table_row_data_client(self):
        """Retrieves 2D list of all table row texts."""
        return self.table.get_table_row_data()

    def get_column_index_client(self, column_name):
        """Returns index of specified column name."""
        return self.table.get_column_index(column_name)

    def check_column_cells_client(self, column_name):
        """Extracts text for all cells in a column."""
        return self.table.check_column_cells(column_name)

    def check_column_cells_not_empty_client(self, column_name):
        """Verifies no cell in target column is empty/blank/dash."""
        return self.table.check_column_cells_not_empty(column_name)

    def expand_tree_row_client(self, row_index):
        """Expands caret row in tree table."""
        return self.table.expand_tree_row(row_index)

    def click_edit_btn_client(self, target):
        """Clicks edit button by index or value target."""
        return self.table.click_edit_btn(target)

    def click_edit_btn_by_row_index_client(self, row_idx=1):
        """Clicks edit button on specific row index."""
        self.table.click_edit_btn_by_row_index(row_idx)
        return True and self

    def click_edit_btn_by_column_value_client(self, column_name, text):
        """Clicks edit button matching a column text value."""
        return self.table.click_edit_btn_by_column_value(column_name, text)

    def check_toggle_status_on_table_client(self, column_name, text):
        """Verifies active/inactive switch state across rows."""
        return self.table.check_toggle_status_on_table(column_name, text)

    def search_in_table_client(self, search_term):
        """Types query term into global table search box."""
        return self.table.search_in_table(search_term)

    def check_table_data_by_search_client(self, column_name, text):
        """Filters table by search and verifies query text exists."""
        return self.table.check_table_data_by_search(column_name, text)

    def check_table_data_by_dropdown_client(self, column_name, text):
        """Filters table by dropdown across pagination pages."""
        return self.table.check_table_data_by_dropdown(column_name, text)

    def verify_no_results_found_client(self, expected_text="No results found"):
        """Checks for table empty state message."""
        return self.table.verify_no_results_found(expected_text)

    def check_table_verify_no_results_client(self, search_term, expected_text="No results found"):
        """Searches invalid term and asserts empty state message."""
        return self.table.check_table_verify_no_results(search_term, expected_text)

    def sort_column_client(self, column_name):
        """Clicks column header to sort table."""
        return self.table.sort_column(column_name)

    def verify_column_sorting_client(self, column_name, order="ascending", is_numeric=False):
        """Verifies sorting sequence on column values."""
        return self.table.verify_column_sorting(column_name, order, is_numeric)

    def change_rows_per_page_client(self, count):
        """Changes pagination row count dropdown."""
        return self.table.change_rows_per_page(count)

    def go_to_next_page_client(self, ):
        """Navigates to next pagination page."""
        return self.table.go_to_next_page()

    def go_to_prev_page_client(self):
        """Navigates to previous pagination page."""
        return self.table.go_to_prev_page()

    def get_pagination_information_client(self):
        """Returns pagination text string (e.g. '1-10 of 50')."""
        return self.table.get_pagination_information()

## ------------------------------------------------------------------------------- ##

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
            self.element.is_component_visible(Update_Modal_Inputs.CONTACT_PERSON_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT),
            self.element.is_component_visible(Update_Modal_Inputs.PHONE_NUMBER_INPUT),  
        ])

    def clear_search_bar(self, locator = Filter_and_Search_Section.SEARCH_BAR):
        return self.clear_input_field(locator)

    def is_client_modal_buttons_visible(self):
        return all ([
            self.element.is_component_visible(Modal_Action_Buttons.CLOSE_BUTTON),
            self.element.is_component_visible(Modal_Action_Buttons.SAVE_BUTTON)
        ])

    def is_client_modal_visible(self):
        return self.element.is_component_visible(Update_Modal_Inputs.MODAL_BODY)

    def is_toast_notification_visible(self):
        return self.element.is_component_visible(Toast_Notifications_Validation_Messages.FIELD_ERROR_MESSAGE)
       
    def is_client_modal_visible(self):
        return self.element.is_component_visible(Update_Modal_Inputs.MODAL_BODY)

    def is_add_client_button_visible(self):
        return self.element.is_component_visible(Client_Locators.ADD_CLIENT_BUTTON)

    def is_search_bar_and_dropdown_visible(self):
        return all([
            self.element.is_component_visible(Filter_and_Search_Section.SEARCH_BAR),
            self.element.is_component_visible(Filter_and_Search_Section.STATUS_FILTER_DROPDOWN),
            self.element.is_component_visible(Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN)
        ])

    def is_pagination_component_visible(self):
        return self.element.is_component_visible(Pagination_Section.PAGINATION_CONTAINER)
    
    def get_table_header_clients(self):
        return self.table.get_table_headers()
    
    def get_table_headers_client(self):
        return self.table.get_table_headers()

    def ensure_element_visible(self, locator):
        """
        Waits until an element is visible in the DOM and returns it.
        Uses the instance's standard explicit wait engine (self.wait).

        """
        return self.wait.until(EC.visibility_of_element_located(locator))

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
        # if industry:
        #     self.select_react_dropdown(Update_Modal_Inputs.INDUSTRY_SELECT, industry)
        #     time.sleep(0.5)
        # if country:
        #     self.select_react_dropdown(Update_Modal_Inputs.COUNTRY_SELECT, country)
        #     time.sleep(0.5)
        self.fill_country_select_modal_client()
        self.fill_industry_select_modal_client()

        # 3. Text Inputs
        self.wait_and_type(Update_Modal_Inputs.CONTACT_PERSON_INPUT, contact)
        self.wait_and_type(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT, email)
        self.wait_and_type(Update_Modal_Inputs.PHONE_NUMBER_INPUT, phone)
        self.wait_and_type(Update_Modal_Inputs.ADDRESS_INPUT, address)

        return True  # Indicate successful form fill

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

        self.clear_input_field(Update_Modal_Inputs.CLIENT_NAME_INPUT)
        self.clear_input_field(Update_Modal_Inputs.CONTACT_PERSON_INPUT)
        self.clear_input_field(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT)
        self.clear_input_field(Update_Modal_Inputs.PHONE_NUMBER_INPUT)
        self.clear_input_field(Update_Modal_Inputs.ADDRESS_INPUT)
        self.wait_and_type(Update_Modal_Inputs.CLIENT_NAME_INPUT, name)
        self.wait_and_type(Update_Modal_Inputs.CONTACT_PERSON_INPUT, contact)
        self.wait_and_type(Update_Modal_Inputs.EMAIL_ADDRESS_INPUT, email)
        self.wait_and_type(Update_Modal_Inputs.PHONE_NUMBER_INPUT, phone)
        self.wait_and_type(Update_Modal_Inputs.ADDRESS_INPUT, address)

        self.fill_country_select_modal_client()
        self.fill_industry_select_modal_client()

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
