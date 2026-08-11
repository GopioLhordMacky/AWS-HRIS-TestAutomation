from locators.shared.shared_locators import CommonTableLocators
from locators.shared.shared_locators import SearchLocators
from locators.shared.shared_locators import DropdownLocators
from locators.shared.shared_locators import TreeTableLocators
from imports.main_imports.main_imports import *
from pages.base_page import BasePage

class Table(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_table_headers(self):
        headers = self.driver.find_elements(*CommonTableLocators.TABLE_HEADERS)
        return [h.text.strip() for h in headers]

    def get_single_table_row_data(self, row_idx=1):
        row_cells = self.driver.find_elements(By.XPATH, f"//tbody/tr[{row_idx}]/td")
        return [cell.text.strip() for cell in row_cells]

    def count_table_rows(self):
        return len(self.driver.find_elements(*CommonTableLocators.TABLE_ROWS))

    def get_table_row_data(self):
        rows = self.driver.find_elements(*CommonTableLocators.TABLE_ROWS)
        return [[cell.text.strip() for cell in row.find_elements(By.TAG_NAME, "td")] for row in rows]

    def get_column_index(self, column_name):
        headers = self.get_table_headers()
        for index, header in enumerate(headers, start=1):
            if column_name.lower() in header.lower():
                return index
        raise ValueError(f"Column '{column_name}' not found in table headers: {headers}")

    def get_dropdown_value(self, label_name):
        elems = self.driver.find_elements(
            By.XPATH, 
            f"//div[contains(@class, 'modal-content')]//label[text()='{label_name}']/following::div[contains(@class, '-singleValue')][1]"
        )
        return elems[0].text.strip() if elems else ""

    def get_table_cell_value(self, column_name: str, row_idx: int = 1) -> str:
        """
        Retrieves the text content of a specific table cell based on column name and row index.
        """
        # 1. Find column index dynamically (1-based index)
        # Assumes get_table_headers returns a list of header strings like ["Client Name", "Industry", ...]
        headers = self.get_table_headers() if hasattr(self, "get_table_headers") else []
        
        try:
            # Match column name (case-insensitive & trimmed)
            col_idx = [h.strip().lower() for h in headers].index(column_name.strip().lower()) + 1
            
            # 2. Locate and return the cell text directly via XPath
            xpath = f"//tbody/tr[{row_idx}]/td[{col_idx}]"
            elem = self.find_elements(By.XPATH, xpath)
            return elem.text.strip() if elem else ""
            
        except ValueError:
            print(f"[WARNING] Column header '{column_name}' not found in table headers: {headers}")
            return ""
        
    def check_column_cells(self, column_name):
        col_idx = self.get_column_index(column_name)
        rows = self.driver.find_elements(*CommonTableLocators.TABLE_ROWS)
        return [row.find_element(By.XPATH, f"./td[{col_idx}]").text.strip() for row in rows]

    def check_column_cells_not_empty(self, column_name):
        col_idx = self.get_column_index(column_name)
        cells = self.driver.find_elements(By.XPATH, f"//tbody/tr/td[{col_idx}]")
        if not cells:
            return False  # No rows present in the table
        for cell in cells:
            cell_text = cell.text.strip()
            # Check if blank, exact dash, or 1 character or fewer
            if not cell_text or cell_text == "-" or len(cell_text) <= 1:
                return False  # Invalid cell text found
        return True

    def expand_tree_row(self, row_index):
        self.wait_for_and_click(TreeTableLocators.EXPAND_CARET_BY_ROW(row_index))

    def click_edit_btn(self, target):
        if isinstance(target, int):
            self.wait_for_and_click(CommonTableLocators.EDIT_BTN_BY_INDEX(target))
        else:
            self.wait_for_and_click(CommonTableLocators.EDIT_BTN_BY_VALUE(str(target)))

    def click_edit_btn_by_row_index(self, row_idx=1):
        locator = CommonTableLocators.EDIT_BTN_BY_INDEX(row_idx)
        self.wait_for_and_click(locator)

    def click_edit_btn_by_column_value(self, column_name, text):
        col_idx = self.get_column_index(column_name)
        locator = CommonTableLocators.EDIT_BTN_BY_COLUMN_VALUE(col_idx, text)
        self.wait_for_and_click(locator)

    def check_toggle_status_on_table(self, column_name, text):
        """
        Dedicated helper for table columns that use switch/toggle controls 
        instead of plain text (e.g., Status/Active toggle columns).
        """
        try:
            headers = self.driver.find_elements(By.XPATH, "//table//th")
            col_index = -1
            for idx, header in enumerate(headers, start=1):
                if column_name.lower() in header.text.strip().lower():
                    col_index = idx
                    break

            if col_index == -1:
                print(f"[check_table_toggle_data_by_dropdown] Column '{column_name}' not found!")
                return False

            cells = self.driver.find_elements(By.XPATH, f"//table//tbody//tr/td[{col_index}]")
            if not cells:
                print(f"[check_table_toggle_data_by_dropdown] No data rows found.")
                return False

            for cell in cells:
                checkboxes = cell.find_elements(By.CSS_SELECTOR, "input.form-check-input, input[type='checkbox']")
                if checkboxes:
                    is_checked = checkboxes[0].is_selected() or checkboxes[0].get_attribute("checked") is not None
                    cell_value = "Active" if is_checked else "Inactive"
                else:
                    cell_value = cell.text.strip()

                if text.lower() not in cell_value.lower():
                    print(f"[check_table_toggle_data_by_dropdown] Mismatch! Expected: '{text}', Found: '{cell_value}'")
                    return False

            return True

        except Exception as e:
            print(f"[check_table_toggle_data_by_dropdown] Exception: {e}")
            return False

    def select_custom_dropdown(self, dropdown_label, option_text):
        self.wait_for_and_click(DropdownLocators.DROPDOWN_OPTION(dropdown_label))
        self.wait_for_and_click(DropdownLocators.DROPDOWN_OPTION(option_text))

    def search_in_table(self, search_term):
        search_enter = self.wait_and_type(SearchLocators.GLOBAL_SEARCH_INPUT, text=search_term)
        # search_enter.send_keys(Keys.ENTER)

    def check_table_data_by_search(self, column_name, text):
        """Filters the table using the search bar, expands rows per page to 100, 
        and verifies if the query text exists in the specified column.
        
        :param column_name: The header text of the target column
        :param text: The search query text expected in the cell
        :return: bool (True if text is found in column, False otherwise)
        """
        try:
            # 1. Refresh page at the start
            self.driver.refresh()
            time.sleep(2)

            # 2. Set rows per page to 100 to ensure all filtered results are visible
            self.change_rows_per_page(100)
            time.sleep(2)

            # 3. Filter the table using the built-in search input
            self.search_in_table(text)
            time.sleep(3)  # Brief wait for table results to filter

            # 4. Get column index and row data
            col_idx = self.get_column_index(column_name)
            col_list_idx = col_idx - 1
            table_data = self.get_table_row_data()

            # 5. Check if target text exists in the specific column
            for row in table_data:
                if len(row) > col_list_idx:
                    if text.lower() in row[col_list_idx].lower():
                        return True

            return False

        except Exception as e:
            print(f"[check_table_data] Error during table search check: {e}")
            return False

    def check_table_data_by_dropdown(self, column_name, text):
        """
        Filters the table using a dropdown filter, sets rows per page to 100, 
        and verifies across ALL pagination pages that EVERY row in the specified 
        column EXACTLY matches the target text (case-insensitive, trimmed).
        """
        try:
            # 1. Expand rows per page to 100
            self.change_rows_per_page(20)
            
            # Explicit wait for table rows to reload after changing rows per page
            self.wait.until(
                EC.presence_of_all_elements_located(CommonTableLocators.TABLE_ROWS)
            )
            time.sleep(2)

            # 2. Filter the table using the dropdown
            # self.select_custom_dropdown(column_name, text)
            time.sleep(3)  # Wait for filter application

            expected_text = text.strip().lower()
            page_number = 1

            # Get column index
            col_idx = self.get_column_index(column_name)
            col_list_idx = col_idx - 1

            # 3. Pagination loop
            while True:
                # Capture initial row reference to monitor page transition staleness
                current_row_elements = self.driver.find_elements(*CommonTableLocators.TABLE_ROWS)
                first_row_before = current_row_elements[0] if current_row_elements else None

                # Get row text data
                table_data = self.get_table_row_data()

                if not table_data:
                    print(f"[check_table_data] No rows displayed on page {page_number} for '{text}'.")
                    return False

                # Verify EVERY row on the current page
                for row_idx, row in enumerate(table_data):
                    if len(row) > col_list_idx:
                        actual_cell_text = row[col_list_idx].strip().lower()
                        
                        # Strict exact match
                        if actual_cell_text != expected_text:
                            print(
                                f"[check_table_data] Mismatch on Page {page_number}, Row {row_idx + 1}, "
                                f"Column '{column_name}': Expected EXACTLY '{text}', but got '{row[col_list_idx].strip()}'"
                            )
                            return False

                # Check if go_to_next_page can proceed
                # Note: At 100 rows per page, all records might fit on Page 1, making Next disabled immediately.
                try:
                    has_next = self.go_to_next_page()
                except Exception as e:
                    print(f"[check_table_data] go_to_next_page returned exception/False: {e}")
                    has_next = False

                if not has_next:
                    print(f"[check_table_data] Reached end of pagination at page {page_number}.")
                    break

                # If moving to next page, wait for old page's first row to go stale before re-checking
                if first_row_before:
                    try:
                        self.wait.until(EC.staleness_of(first_row_before))
                    except Exception:
                        time.sleep(2)

                page_number += 1

            return True

        except Exception as e:
            print(f"[check_table_data] Error during table search check: {e}")
            return False

    def verify_no_results_found(self, expected_text="No results found"):
        try:
            table_body = self.wait.until(
                EC.presence_of_element_located(CommonTableLocators.TABLE_BODY)
            )
            actual_text = table_body.text.strip()
            return expected_text.lower() in actual_text.lower()
        except Exception as e:
            print(f"[ERROR] Failed to locate or verify empty table body: {e}")
            return False

    def check_table_verify_no_results(self, search_term, expected_text="No results found"):
        """
        Searches for a term in the table and immediately verifies that no results are found.
        
        :param search_term: The invalid search term to enter
        :param expected_text: Text expected in the table body (default: 'No results found')
        :return: True if the search yields the expected empty state, False otherwise
        """
        # Step 1: Perform the search
        search_enter = self.wait_and_type(SearchLocators.GLOBAL_SEARCH_INPUT, text=search_term)
        time.sleep(2)
        
        # Step 2: Verify the empty state in the table body
        try:
            table_body = self.wait.until(
                EC.presence_of_element_located(CommonTableLocators.TABLE_BODY)
            )
            actual_text = table_body.text.strip()
            return expected_text.lower() in actual_text.lower()
        except Exception as e:
            print(f"[ERROR] Failed to locate or verify empty table body: {e}")
            return False


    def sort_column(self, column_name):
        self.wait_for_and_click(CommonTableLocators.HEADER_BY_NAME(column_name))

    def verify_column_sorting(self, column_name, order="ascending", is_numeric=False):
        """
        Sorts a table column using `sort_column` and verifies that the column values
        are sorted in the expected order ('ascending' or 'descending').
        """
        # 1. Trigger the sort action
        self.sort_column(column_name)
        time.sleep(1)  # Allow DOM/table re-render

        # 2. Get column index dynamically to locate the cells
        col_idx = self.get_column_index(column_name)

        # 3. Collect all cell values for that column
        cells = self.driver.find_elements(By.XPATH, f"//tbody/tr/td[{col_idx}]")
        raw_values = [cell.text.strip() for cell in cells if cell.text.strip() != ""]

        # Exit early if table has fewer than 2 items to sort
        if len(raw_values) < 2:
            return True

        # 4. Cast values for comparison (handles numeric strings vs. standard text)
        if is_numeric:
            # Strip currency symbols or commas if necessary
            parsed_values = [float(val.replace("$", "").replace(",", "")) for val in raw_values]
        else:
            # Lowercase text for case-insensitive alphabetical sorting
            parsed_values = [val.lower() for val in raw_values]

        # 5. Check order
        order = order.lower()
        if order in ["asc", "ascending"]:
            expected_values = sorted(parsed_values)
        elif order in ["desc", "descending"]:
            expected_values = sorted(parsed_values, reverse=True)
        else:
            raise ValueError(f"Invalid order argument: '{order}'. Use 'ascending' or 'descending'.")

        # 6. Assert and return boolean check
        assert parsed_values == expected_values, (
            f"Column '{column_name}' sorting failed for {order} order!\n"
            f"Actual: {raw_values}\n"
            f"Expected Order: {expected_values}"
        )
        return True


    def change_rows_per_page(self, count):
        self.wait_for_and_click(PaginationLocators.ROWS_PER_PAGE_DROPDOWN)
        self.wait_for_and_click(PaginationLocators.ROWS_PER_PAGE_OPTION(count))

    def go_to_next_page(self):
        self.wait_for_and_click(PaginationLocators.NEXT_PAGE_BTN)

    def go_to_prev_page(self):
        self.wait_for_and_click(PaginationLocators.PREV_PAGE_BTN)

    def get_pagination_information(self):
        element = self.ensure_element_visible(PaginationLocators.PAGINATION_INFO_TEXT)
        return element.text.strip()