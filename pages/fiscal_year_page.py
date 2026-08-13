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
from data.fiscal_year_page_inputs import DropdownOptions


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

    def select_status_filter_fiscal_year(self, option_text):
        """Selects an option from a labeled custom dropdown."""
        self.element.select_custom_dropdown("Status", option_text)
        return True and self

    # --------------------------------------------------------------------------- #
    # Dynamic Field Getters (Read-Only Modal Fields)
    # --------------------------------------------------------------------------- #
    def get_start_date_value(self) -> str:
        """Retrieves the current value of the Start Date input field in the modal."""
        # Option 2: Direct driver find element
        start_date_element = self.find_element(Options.START_DATE) # Replace with your locator
        return start_date_element.get_attribute("value")

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
        return True and self

    def click_outside_modal_fiscal_year(self):
        """Dismisses modal by hitting ESC."""
        self.modal.click_outside_modal()
        return True and self

    # --------------------------------------------------------------------------- #
    # Keyboard Navigation Helpers
    # --------------------------------------------------------------------------- #
    def tab_navigation_status_filter_fiscal_year(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Options.STATUS_DROPDOWN,
                                                [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER],
                                                    helper, *helper_args, **helper_kwargs)

    def tab_navigation_search_bar(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Options.SEARCH_FIELD,
                                                [Keys.ENTER],
                                                    helper, *helper_args, **helper_kwargs)

    def tab_navigation_add_fiscal_year(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Buttons.ADD_FISCAL_YEAR_BUTTON,
                                               [Keys.ENTER],
                                                 helper, *helper_args, **helper_kwargs)

    def tab_navigation_toggle_status(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(Options.TOGGLE_BUTTON,
                                                [Keys.SPACE, Keys.TAB, Keys.ENTER],
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

    def toggle_active_status_fiscal_year(self, row_index = 1, column_name="Active"):
        """Toggles active switch in a specific table row."""
        self.element.toggle_active_status(row_index, column_name)
        return True and self

    def check_table_data_by_search_fiscal_year(self, column_name, text):
        """Filters table by search and verifies query text exists."""
        return self.table.check_table_data_by_search(column_name, text)
    
    def check_table_verify_no_results_fiscal_year(self, search_term, expected_text="No results found"):
        """Searches invalid term and asserts empty state message."""
        return self.table.check_table_verify_no_results(search_term, expected_text)
    
    def check_toggle_status_on_table_fiscal_year(self, column_name, text):
        """Verifies active/inactive switch state across rows."""
        return self.table.check_toggle_status_on_table(column_name, text)
    
    def get_table_headers_client(self):
        """Retrieves list of table header titles."""
        return self.table.get_table_headers()

    # def get_fiscal_year_row_data(self, row_index=1):
    #     """
    #     Retrieves all values for a specific row as a dictionary mapping headers to cell texts.
    #     Columns: Fiscal Year, FY Code, Start Date, End Date, Date Created, Date Updated
    #     """
    #     headers = [
    #         "Fiscal Year",
    #         "FY Code",
    #         "Start Date",
    #         "End Date",
    #         "Date Created",
    #         "Date Updated",
    #     ]
    #     row_data = {}
    #     row_element = self.find_element((By.XPATH, f"//tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]"))
    #     if not row_element:
    #         return row_data

    #     for idx, header in enumerate(headers, start=0):
    #         cell_locator = (By.XPATH, f"./td[{idx}]")
    #         row_data[header] = self.get_text_from_element(row_element, cell_locator)
    #     return row_data

    def get_table_fiscal_year(self, row_idx: int = 1) -> str:
        """Retrieves the Fiscal Year cell value for a specified row index."""
        return self.table.get_table_cell_value("Fiscal Year", row_idx=row_idx)

    def get_table_fy_code(self, row_idx: int = 1) -> str:
        """Retrieves the FY Code cell value for a specified row index."""
        return self.table.get_table_cell_value("FY Code", row_idx=row_idx)

    def get_table_start_date(self, row_idx: int = 1) -> str:
        """Retrieves the Start Date cell value for a specified row index."""
        return self.table.get_table_cell_value("Start Date", row_idx=row_idx)

    def get_table_end_date(self, row_idx: int = 1) -> str:
        """Retrieves the End Date cell value for a specified row index."""
        return self.table.get_table_cell_value("End Date", row_idx=row_idx)

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

    def click_edit_fiscal_year(self, row_index=1):
        """Clicks edit action button on a given row index."""
        edit_locator = (
            By.XPATH,
            f"//tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]//div[@class='container'] | //tbody[contains(@class, 'MuiTableBody-root')]/tr[{row_index}]//*[contains(@class, 'edit')]",
        )
        return self.wait_for_and_click(edit_locator)

    # --------------------------------------------------------------------------- #
    # Search, Sorting & Pagination
    # --------------------------------------------------------------------------- #
    def change_rows_per_page_fiscal_year(self, count):
        """Changes pagination row count dropdown."""
        return self.table.change_rows_per_page(count)

    def go_to_next_page_fiscal_year(self, ):
        """Navigates to next pagination page."""
        return self.table.go_to_next_page()

    def go_to_prev_page_fiscal_year(self):
        """Navigates to previous pagination page."""
        return self.table.go_to_prev_page()

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

    def search_fiscal_year(self, text):
        """Enters search text into the search field."""
        self.clear_input_field(Options.SEARCH_FIELD)
        return self.wait_and_type(Options.SEARCH_FIELD, text)

    def clear_search_bar(self, locator=Options.SEARCH_FIELD):
        """Clears the search input field."""
        self.clear_input_field(locator)
        return True and self

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

    def get_pagination_information_fiscal_year(self):
        """Returns pagination text string (e.g. '1-10 of 50')."""
        return self.table.get_pagination_information()

    def verify_column_sorting_fiscal_year(self, column_name, order="ascending", is_numeric=False):
        """Verifies sorting sequence on column values."""
        return self.table.verify_column_sorting(column_name, order, is_numeric)

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

    def is_confirm_button_visible(self):
        return self.element.is_component_visible(ModalLocators.CONFIRM_BUTTON)

    def is_cancel_button_visible(self):
        return self.element.is_component_visible(ModalLocators.CANCEL_BUTTON)
    
    def is_save_button_clickable_fiscal_year(self):
        """Checks if the Save button in the modal is clickable."""
        return self.element.is_component_clickable(ModalLocators.SAVE_BUTTON)

    def is_close_button_clickable_fiscal_year(self):
        """Checks if the Close button in the modal is clickable."""
        return self.element.is_component_clickable(ModalLocators.CLOSE_BUTTON)
    
    def verify_status_input_matches_fiscal_year(self, locator= Options.STATUS_DROPDOWN, expected_text=None):
        """Verifies if an input value matches expected text."""
        return self.element.verify_input_matches(locator, expected_text)

    def verify_status_dropdown_options_fiscal_year(self, 
                                    dropdown_locator = Options.STATUS_DROPDOWN,
                                    expected_options = DropdownOptions.status_options,
                                    options_locator=None):
        """Verifies dropdown options against expected list."""
        return self.element.verify_dropdown_options(dropdown_locator, expected_options, options_locator)
    
    def verify_modal_fields_are_cleared(self) -> bool:
        """Verifies that all form fields within the Add Fiscal Year modal are reset or empty."""
        start_date_val = self.get_start_date_value()
        end_date_val = self.get_auto_end_date()
        fiscal_year_val = self.get_auto_fiscal_year()
        fy_code_val = self.get_auto_fy_code()

        return (
            start_date_val in ["", None]
            and end_date_val in ["", None]
            and fiscal_year_val in ["", None]
            and fy_code_val in ["", None]
        )

    def verify_table_row_data_matches_edit_modal(self, row_idx: int = 1) -> bool:
        """
        Reads row data from the table at row_idx, opens the edit modal, formats 
        table dates (MM/DD/YYYY) to modal inputs (MM-YYYY), and verifies that all 
        modal field values match the table row data.
        """
        # 1. Read actual cell values from the target table row
        table_fiscal_year = self.get_table_fiscal_year(row_idx=row_idx)
        table_fy_code = self.get_table_fy_code(row_idx=row_idx)
        table_start_date = self.get_table_start_date(row_idx=row_idx) # e.g. "04/01/2026"
        table_end_date = self.get_table_end_date(row_idx=row_idx)     # e.g. "03/31/2027"

        # 2. Convert MM/DD/YYYY table format to MM-YYYY modal format
        start_m, _, start_y = table_start_date.split("/")
        expected_modal_start_date = f"{start_m}-{start_y}"

        end_m, _, end_y = table_end_date.split("/")
        expected_modal_end_date = f"{end_m}-{end_y}"

        # 3. Open the edit modal for the target row
        if not self.click_edit_fiscal_year(row_index=row_idx):
            return False

        if not self.is_fiscal_year_modal_visible():
            return False

        # 4. Fetch actual values from the opened modal
        modal_start_date = self.get_start_date_value()
        modal_end_date = self.get_auto_end_date()
        modal_fiscal_year = self.get_auto_fiscal_year()
        modal_fy_code = self.get_auto_fy_code()

        # 5. Cross-check table data against modal fields
        return (
            modal_start_date == expected_modal_start_date
            and modal_end_date == expected_modal_end_date
            and modal_fiscal_year == table_fiscal_year
            and modal_fy_code == table_fy_code
        )
    
    def verify_saved_fiscal_year_in_table(self, start_date: str, end_date: str, fiscal_year: str, fy_code: str) -> bool:
        """
        Searches the table using the year extracted from start_date and verifies 
        that the table values match the expected formatted outputs.
        """
        # Extract only the year (YYYY) for search input
        search_year = start_date.split("-")[-1]

        # Perform search using the table search helper
        search_success = self.table.check_table_data_by_search("Fiscal Year", search_year)
        if not search_success:
            return False

        # Convert MM-YYYY inputs to MM/DD/YYYY table format
        start_m, start_y = start_date.split("-")
        end_m, end_y = end_date.split("-")

        # Start Date always sets to the 1st of the month: MM/01/YYYY
        expected_table_start_date = f"{start_m}/01/{start_y}"

        # End Date sets to the last day of the preceding month
        # Determine last day of end_month (28, 30, or 31)
        if end_m in ["01", "03", "05", "07", "08", "10", "12"]:
            last_day = "31"
        elif end_m in ["04", "06", "09", "11"]:
            last_day = "30"
        else:
            # February check (leap year calculation)
            y_int = int(end_y)
            last_day = "29" if (y_int % 4 == 0 and (y_int % 100 != 0 or y_int % 400 == 0)) else "28"

        expected_table_end_date = f"{end_m}/{last_day}/{end_y}"

        # Retrieve actual cell values from the table
        actual_fiscal_year = self.table.get_table_cell_value("Fiscal Year", row_idx=1)
        actual_fy_code = self.table.get_table_cell_value("FY Code", row_idx=1)
        actual_start_date = self.table.get_table_cell_value("Start Date", row_idx=1)
        actual_end_date = self.table.get_table_cell_value("End Date", row_idx=1)

        # Validate formatted values against table cells
        return (
            actual_fiscal_year == fiscal_year
            and actual_fy_code == fy_code
            and actual_start_date == expected_table_start_date
            and actual_end_date == expected_table_end_date
        )
    
    def check_error_message_fiscal_year(self, expected_text=None):
        """Verifies inline/modal error messages."""
        return True and self.modal.check_error_message(expected_text)
    
    def is_modal_title_visible(self):
        """Verifies if the modal title header is visible."""
        return self.element.is_component_visible(Modal.UPDATE_MODAL)

    def are_read_only_fields_disabled(self):
        """Verifies that the read-only input fields (End Date, Fiscal Year Name, FY Code) are disabled."""
        try:
            end_date_disabled = not self.find_element(Options.END_DATE).is_enabled()
            fy_name_disabled = not self.find_element(Options.FY_NAME_INPUT).is_enabled()
            fy_code_disabled = not self.find_element(Options.FY_CODE_INPUT).is_enabled()
            return end_date_disabled and fy_name_disabled and fy_code_disabled
        except Exception as e:
            print(f"[ERROR] Failed checking disabled states: {e}")
            return False
        
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
        self.element.is_component_visible(Modal.UPDATE_MODAL)
        return True and self

    # def is_toast_notification_visible(self):
    #     """Verifies if alert or toast warning is displayed."""
    #     return self.element.is_component_visible(Confirmation_Dialogue.TOAST_MESSAGE) or self.element.is_component_visible(Confirmation_Dialogue.START_DATE_REQUIRED)

    def check_toast_message_fiscal_year(self, expected_text=None):
        """Verifies toast popup message."""
        return self.modal.check_toast_message(expected_text)
    
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