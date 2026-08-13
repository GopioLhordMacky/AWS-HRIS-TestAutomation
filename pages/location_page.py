import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.location_page_locators import (Options, Modals)
from pages.base_page import BasePage
from components.tables import Table
from components.elements import Element
from components.modals import Modals
from components.navigation import Navigation

class LocationPage(BasePage):
    """Page Object Model for the Location Page."""

    def __init__(self, driver):
        super().__init__(driver) 
        self.table = Table(driver)   
        self.element = Element(driver)           
        self.navigation = Navigation(driver)
        self.modal = Modals(driver)

 # ==========================================
    # Unique Location Page Handlers
    # ==========================================
    def expand_row_tree_location(self, row_index=1):
        """Expands a tree node row using the table component method."""
        self.table.expand_tree_row(row_index)
        return self

    def open_add_location_dropdown(self):
        """Clicks '+ Add Location' dropdown button."""
        self.element.is_component_clickable(Options.ADD_LOCATION_DROPDOWN_BUTTON)
        self.driver.find_element(*Options.ADD_LOCATION_DROPDOWN_BUTTON).click()
        return self

    def open_add_country_modal(self):
        self.open_add_location_dropdown()
        self.driver.find_element(*Options.ADD_COUNTRY_BUTTON).click()
        return self

    def open_add_province_modal(self):
        self.open_add_location_dropdown()
        self.driver.find_element(*Options.ADD_PROVINCE_BUTTON).click()
        return self

    def open_add_city_modal(self):
        self.open_add_location_dropdown()
        self.driver.find_element(*Options.ADD_CITY_BUTTON).click()
        return self

    def fill_country(self, country_name):
        """Clicks React-Select container for country, types name, and hits ENTER."""
        select_container = self.driver.find_element(*Options.SELECT_COUNTRY)
        select_container.click()
        time.sleep(0.3)
        input_elem = select_container.find_element(By.XPATH, ".//input")
        input_elem.send_keys(country_name)
        time.sleep(0.5)
        input_elem.send_keys(Keys.ENTER)
        return self

    def fill_province(self, province_name):
        """Clicks React-Select container for province, types name, and hits ENTER."""
        select_container = self.driver.find_element(*Options.SELECT_PROVINCE)
        select_container.click()
        time.sleep(0.3)
        input_elem = select_container.find_element(By.XPATH, ".//input")
        input_elem.send_keys(province_name)
        time.sleep(0.5)
        input_elem.send_keys(Keys.ENTER)
        return self

    def fill_city(self, city_name):
        """Clicks React-Select container for city, types name, and hits ENTER."""
        select_container = self.driver.find_element(*Options.SELECT_CITY)
        select_container.click()
        time.sleep(0.3)
        input_elem = select_container.find_element(By.XPATH, ".//input")
        input_elem.send_keys(city_name)
        time.sleep(0.5)
        input_elem.send_keys(Keys.ENTER)
        return self

    # ==========================================
    # Filter & Search Methods
    # ==========================================
    def select_type_filter_location(self, option_text):
        """Selects an option from the 'Type' dropdown using Elements component."""
        self.element.select_custom_dropdown("Type", option_text)
        return self

    def select_status_filter_location(self, option_text):
        """Selects an option from the 'Status' dropdown using Elements component."""
        self.element.select_custom_dropdown("Status", option_text)
        return self

    def search_location(self, text):
        """Searches table entries using Table component."""
        self.table.search_in_table(text)
        return self

    # ==========================================
    # Read-Only Field Getters
    # ==========================================
    def get_auto_iso_code(self):
        return self.driver.find_element(*Options.ISO_CODE).get_attribute("value")

    def get_auto_state_code(self):
        return self.driver.find_element(*Options.ISO_CODE).get_attribute("value")

    # ==========================================
    # Modal Control Actions (Delegated to Modals component)
    # ==========================================
    def click_close_modal_location(self):
        self.modal.click_close()
        return self

    def click_confirm_modal_location(self):
        self.modal.click_confirm()
        return self

    def click_cancel_modal_location(self):
        self.modal.click_cancel()
        return self

    def click_save_only_modal_location(self):
        self.modal.click_save_only()
        return self

    def click_save_confirm_modal_location(self):
        self.modal.click_save_confirm()
        return self

    def click_close_x_modal_location(self):
        self.modal.click_close_x()
        return self

    def click_outside_modal_location(self):
        self.modal.click_outside_modal()
        return self

    # ==========================================
    # Table Component Utilities (Delegated to Tables component)
    # ==========================================
    def get_table_headers_location(self):
        return self.table.get_table_headers()

    def get_location_row_data(self, row_index=1):
        return self.table.get_single_table_row_data(row_idx=row_index)

    def get_location_value(self, column_name, row_index=1):
        return self.table.get_table_cell_value(column_name=column_name, row_idx=row_index)

    def get_location_table_row_count(self):
        return self.table.count_table_rows()

    def get_full_location_table_data(self):
        return self.table.get_table_row_data()

    def is_table_empty(self):
        return self.table.count_table_rows() == 0

    def click_location_table_header(self, column_name):
        self.table.sort_column(column_name)
        return self

    def select_rows_per_page(self, count):
        self.table.change_rows_per_page(count)
        return self

    def click_next_page(self):
        self.table.go_to_next_page()
        return self

    def click_previous_page(self):
        self.table.go_to_prev_page()
        return self

    def get_pagination_summary(self):
        return self.table.get_pagination_information()

    # ==========================================
    # Visibility Assertions & Validations
    # ==========================================
    def is_country_modal_visible(self):
        """Checks if the Add Country modal is visible."""
        return self.element.is_component_visible()

    def is_province_modal_visible(self):
        """Checks if the Add Province modal is visible."""
        return self.element.is_component_visible(Modals.PROVINCE_MODAL)

    def is_city_modal_visible(self):
        """Checks if the Add City modal is visible."""
        return self.element.is_component_visible(Modals.CITY_MODAL)
    
    def is_location_title_visible(self):
        return self.element.is_component_visible(Options.LOCATION_OPTIONS)

    def is_location_modal_inputs_visible(self):
        return self.element.is_component_visible(Options.SELECT_COUNTRY)

    def is_location_modal_buttons_visible(self):
        return self.element.is_component_visible(Options.SAVE_BUTTON) and \
               self.element.is_component_visible(Options.CLOSE_BUTTON)

    def is_add_location_button_visible(self):
        return self.element.is_component_visible(Options.ADD_LOCATION_DROPDOWN_BUTTON)

    def is_search_bar_and_dropdown_visible(self):
        return self.element.is_component_visible(Options.SEARCH_BAR) and \
               self.element.is_component_visible(Options.TYPE_LABEL)

    def is_pagination_component_visible(self):
        return self.element.is_component_visible(Options.BODY)

    def verify_location_modal_fields_are_empty(self):
        return self.element.verify_input_is_empty(Options.SELECT_COUNTRY)

    def check_error_message_location(self, expected_text=None):
        return self.modal.check_error_message(expected_text)

    def check_toast_message_location(self, expected_text=None):
        return self.modal.check_toast_message(expected_text)