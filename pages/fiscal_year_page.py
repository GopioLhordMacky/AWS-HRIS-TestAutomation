from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.fiscal_year_page_locators import *
from imports.main_imports import *
from pages.base_page import BasePage
from components.tables import Table
from components.elements import Element
from components.modals import Modals
from components.navigation import Navigation


class FiscalYearPage(BasePage):
    """Page Object Model for the Fiscal Year Page."""

    def __init__(self, driver):
        super().__init__(driver) 
        self.table = Table(driver)   
        self.element = Element(driver)           
        self.navigation = Navigation(driver)
        self.modal = Modals(driver)

# --------------------------------------------------------------------------- #
    # Navigation & Sidebar Helpers
    # --------------------------------------------------------------------------- #

    def open_url(self, url):
        """Navigates directly to the specified URL."""
        self.driver.get(url)

    def check_console_error_fiscal_year(self):
        """Checks browser console for errors."""
        return self.get_browser_console_errors()

    def navigate_to_fiscal_year_page(self):
        """Navigates to the Fiscal Year page via sidebar menu."""
        try:
            self.wait_for_and_click(Sidebar_Locators.SIDEBAR_MENU)
            self.wait_for_and_click(Sidebar_Locators.FISCAL_YEAR_BUTTON)
            return True
        except Exception as e:
            print(f"[ERROR] Failed to navigate to Fiscal Year page: {e}")
            return False

    def click_add_fiscal_year_button(self):
        """Clicks the Add Fiscal Year button."""
        return self.wait_for_and_click(Buttons.ADD_FISCAL_YEAR_BUTTON)

    def get_add_fiscal_year_button_text(self):
        """Retrieves the label text of the Add Fiscal Year button."""
        return self.get_text(Buttons.ADD_FISCAL_YEAR_BUTTON)

    def is_field_required(self, field_locator):
        """Checks if an input field displays a required indicator or alert."""
        return self.element.is_component_visible(Confirmation_Dialogue.START_DATE_REQUIRED)

    # --------------------------------------------------------------------------- #
    # Status Filter Method
    # --------------------------------------------------------------------------- #

    def select_status_filter(self, status_name):
        """Selects an option from the main Status filter dropdown (Active / Inactive)."""
        try:
            dropdown = self.ensure_element_visible(Options.STATUS_DROPDOWN)
            options = dropdown.find_elements(By.TAG_NAME, "option")
            for option in options:
                if option.text.strip().lower() == status_name.lower():
                    option.click()
                    return True
            return False
        except Exception as e:
            print(f"[ERROR] Failed to select status '{status_name}': {e}")
            return False

    # --------------------------------------------------------------------------- #
    # Dynamic Field Getters (Read-Only Modal Fields)
    # --------------------------------------------------------------------------- #

    def get_auto_end_date(self):
        """Gets the calculated value from the read-only End Date field in the modal."""
        return self.get_values_from_locators({"end_date": Options.END_DATE}).get("end_date", "")

    def get_auto_fiscal_year(self):
        """Gets the calculated value from the read-only Fiscal Year field in the modal."""
        return self.get_values_from_locators({"fiscal_year": Options.FY_NAME_INPUT}).get("fiscal_year", "")

    def get_auto_fy_code(self):
        """Gets the calculated value from the read-only FY Code field in the modal."""
        return self.get_values_from_locators({"fy_code": Options.FY_CODE_INPUT}).get("fy_code", "")

    # --------------------------------------------------------------------------- #
    # Modal Control Actions
    # --------------------------------------------------------------------------- #

    def click_close_modal_fiscal_year(self):
        """Clicks close button in modal."""
        if self.modal:
            self.modal.click_close()
        else:
            self.wait_for_and_click(Buttons.CLOSE_BUTTON)
        return True and self

    def click_confirm_modal_fiscal_year(self):
        """Clicks confirm button in modal dialog."""
        if self.modal:
            self.modal.click_confirm()
        else:
            self.wait_for_and_click(Confirmation_Dialogue.CONFIRM_BUTTON)
        return self

    def click_cancel_modal_fiscal_year(self):
        """Clicks cancel button in modal."""
        if self.modal:
            self.modal.click_cancel()
        else:
            self.wait_for_and_click(Confirmation_Dialogue.CANCEL_BUTTON)
        return True and self

    def click_save_only_modal_fiscal_year(self):
        """Clicks save button in modal."""
        if self.modal:
            self.modal.click_save_only()
        else:
            self.wait_for_and_click(Buttons.SAVE_BUTTON)
        return True and self

    def click_save_confirm_modal_fiscal_year(self):
        """Clicks save and then secondary confirm button."""
        if self.modal:
            self.modal.click_save_confirm()
        else:
            self.click_save_only_modal_fiscal_year()
            self.click_confirm_modal_fiscal_year()
        return self

    def click_close_x_modal_fiscal_year(self):
        """Clicks header X button on modal."""
        if self.modal:
            self.modal.click_close_x()
        else:
            self.wait_for_and_click(Buttons.X_BUTTON)
        return self

    def click_outside_modal_fiscal_year(self):
        """Clicks outside the modal dialog overlay to dismiss."""
        try:
            backdrop_locator = (By.XPATH, "//div[contains(@class, 'modal-backdrop') or contains(@class, 'MuiBackdrop-root')]")
            self.wait_for_and_click(backdrop_locator)
            return True and self
        except Exception as e:
            print(f"[ERROR] Failed to click outside modal: {e}")
            return self

    # --------------------------------------------------------------------------- #
    # Keyboard Navigation Helpers
    # --------------------------------------------------------------------------- #

    def press_tab_key(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    def press_shift_tab_key(self):
        self.driver.switch_to.active_element.send_keys(Keys.SHIFT, Keys.TAB)

    def press_enter_key(self):
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def press_arrow_down(self):
        self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)

    def press_spacebar(self):
        self.driver.switch_to.active_element.send_keys(Keys.SPACE)

    # --------------------------------------------------------------------------- #
    # Table Component Utilities
    # --------------------------------------------------------------------------- #

    def get_table_headers_client(self):
        """Retrieves list of table header titles."""
        return self.table.get_table_headers()

    def get_fiscal_year_row_data(self, row_index=1):
        """
        Retrieves all values for a specific row as a dictionary mapping headers to cell texts.
        Columns: Fiscal Year, FY Code, Start Date, End Date, Date Created, Date Updated
        """
        headers = [
            "Fiscal Year",
            "FY Code",
            "Start Date",
            "End Date",
            "Date Created",
            "Date Updated",
        ]
        row_data = {}
        row_element = self.find_element((By.XPATH, f"//tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]"))
        if not row_element:
            return row_data

        for idx, header in enumerate(headers, start=1):
            cell_locator = (By.XPATH, f"./td[{idx}]")
            row_data[header] = self.get_text_from_element(row_element, cell_locator)
        return row_data

    def get_fiscal_year_value(self, column_name, row_index=1):
        """
        Gets a specific cell value by column name and row index using dictionary mapping.
        """
        data = self.get_fiscal_year_row_data(row_index)
        return data.get(column_name, "")

    def get_fiscal_year_table_row_count(self):
        """Returns total visible rows in the table."""
        rows = self.find_elements(Table.TABLE_ROWS)
        return len(rows) if rows else 0

    def get_full_fiscal_year_table_data(self):
        """Returns a list of dictionaries for all rows in the table."""
        total_rows = self.get_fiscal_year_table_row_count()
        return [self.get_fiscal_year_row_data(i) for i in range(1, total_rows + 1)]

    def click_edit_fiscal_year_by_row(self, row_index=1):
        """Clicks edit action button on a given row index."""
        edit_locator = (
            By.XPATH,
            f"//tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]//div[@class='container'] | //tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]//*[contains(@class, 'edit')]",
        )
        return self.wait_for_and_click(edit_locator)

    # --------------------------------------------------------------------------- #
    # Search, Sorting & Pagination
    # --------------------------------------------------------------------------- #

    def search_fiscal_year(self, text):
        """Enters search text into the search field."""
        self.clear_input_field(Options.SEARCH_FIELD)
        return self.wait_and_type(Options.SEARCH_FIELD, text)

    def clear_search_bar(self, locator=Options.SEARCH_FIELD):
        """Clears the search input field."""
        return self.clear_input_field(locator)

    def is_table_empty(self):
        """Checks if the table contains no data rows."""
        return self.get_fiscal_year_table_row_count() == 0

    def click_fiscal_year_table_header(self, column_name):
        """Clicks a table header column for sorting."""
        header_locator = (By.XPATH, f"//thead//th[contains(., '{column_name}')]")
        return self.wait_for_and_click(header_locator)

    def select_rows_per_page(self, count):
        """Selects rows per page count in pagination."""
        self.wait_for_and_click(Pagination.ROWS_PER_PAGE_DROPDOWN)
        option_locator = (By.XPATH, Pagination.ROWS_PER_PAGE_OPTION[1].format(count=count))
        return self.wait_for_and_click(option_locator)

    def click_next_page(self):
        """Clicks next page pagination button."""
        return self.wait_for_and_click(Pagination.NEXT_PAGE_BUTTON)

    def click_previous_page(self):
        """Clicks previous page pagination button."""
        return self.wait_for_and_click(Pagination.PREVIOUS_PAGE_BUTTON)

    def get_pagination_summary(self):
        """Retrieves pagination summary text (e.g. '1-13 of 13')."""
        return self.get_text(Pagination.DISPLAYED_ROWS_TEXT)

    # --------------------------------------------------------------------------- #
    # Form Automation & Data Entry
    # --------------------------------------------------------------------------- #

    def fill_fiscal_year_form(self, start_date):
        """
        Fills out the Fiscal Year modal form (Add).
        Accepts start_date (MM-YYYY e.g., '04-2025').
        """
        self.wait_and_type(Options.START_DATE, start_date)
        return True

    def update_fiscal_year_form(self, start_date):
        """
        Updates the Fiscal Year modal form (Update).
        """
        self.clear_input_field(Options.START_DATE)
        self.wait_and_type(Options.START_DATE, start_date)
        return True

    # --------------------------------------------------------------------------- #
    # Visibility Assertions & Validations
    # --------------------------------------------------------------------------- #

    def is_page_title_visible(self):
            """Verifies visibility of the Fiscal Year page title/header."""
            return self.element.is_component_visible(Login_Locators.FISCAL_YEAR_TITLE)
    
    def is_fiscal_year_modal_inputs_visible(self):
        """Verifies visibility of modal input fields."""
        return all(
            [
                self.element.is_component_visible(Options.START_DATE),
                self.element.is_component_visible(Options.END_DATE),
                self.element.is_component_visible(Options.FY_NAME_INPUT),
                self.element.is_component_visible(Options.FY_CODE_INPUT),
            ]
        )

    def is_fiscal_year_modal_buttons_visible(self):
        """Verifies visibility of Close and Save buttons in modal."""
        return all(
            [
                self.element.is_component_visible(Buttons.CLOSE_BUTTON),
                self.element.is_component_visible(Buttons.SAVE_BUTTON),
            ]
        )

    def is_fiscal_year_modal_visible(self):
        """Verifies if the Fiscal Year modal body is visible."""
        return self.element.is_component_visible(Modal.UPDATE_MODAL)

    def is_toast_notification_visible(self):
        """Verifies if alert or toast warning is displayed."""
        return self.element.is_component_visible(Confirmation_Dialogue.TOAST_MESSAGE) or self.element.is_component_visible(Confirmation_Dialogue.START_DATE_REQUIRED)

    def is_add_fiscal_year_button_visible(self):
        """Verifies visibility of Add Fiscal Year button."""
        return self.element.is_component_visible(Buttons.ADD_FISCAL_YEAR_BUTTON)

    def is_search_bar_and_dropdown_visible(self):
        """Verifies visibility of main search field and status filter dropdown."""
        return all(
            [
                self.element.is_component_visible(Options.SEARCH_FIELD),
                self.element.is_component_visible(Options.STATUS_DROPDOWN),
            ]
        )

    def is_pagination_component_visible(self):
        """Verifies pagination controls visibility."""
        return all(
            [
                self.element.is_component_visible(Pagination.ROWS_PER_PAGE_DROPDOWN),
                self.element.is_component_visible(Pagination.DISPLAYED_ROWS_TEXT),
            ]
        )

    def verify_fiscal_year_modal_fields_are_empty(self):
        """
        Verifies that all modal fields are empty using self.get_values_from_locators.
        """
        locators_map = {
            "Start Date": Options.START_DATE,
            "End Date": Options.END_DATE,
            "Fiscal Year": Options.FY_NAME_INPUT,
            "FY Code": Options.FY_CODE_INPUT,
        }
        values = self.get_values_from_locators(locators_map)
        for field_name, val in values.items():
            if val.strip() != "":
                print(f"[Fiscal Year Check Failed] '{field_name}' field was expected to be empty, but contained data: '{val}'")
                return False

        return True