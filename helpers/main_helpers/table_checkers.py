from locators.shared.shared_locators import CommonTableLocators
from locators.shared.shared_locators import SearchLocators
from locators.shared.shared_locators import DropdownLocators
from locators.shared.shared_locators import TreeTableLocators
from helpers.main_helpers.setup_browser import wait_for_and_click, wait_and_type
from helpers.main_helpers.paginations import *
from imports.main_imports.main_imports import *

def get_table_headers(driver):
    headers = driver.find_elements(*CommonTableLocators.TABLE_HEADERS)
    return [h.text.strip() for h in headers]

def get_single_table_row_data(driver, row_idx=1):
    row_cells = driver.find_elements(By.XPATH, f"//tbody/tr[{row_idx}]/td")
    return [cell.text.strip() for cell in row_cells]

def count_table_rows(driver):
    return len(driver.find_elements(*CommonTableLocators.TABLE_ROWS))

def get_table_row_data(driver):
    rows = driver.find_elements(*CommonTableLocators.TABLE_ROWS)
    return [[cell.text.strip() for cell in row.find_elements(By.TAG_NAME, "td")] for row in rows]

def get_column_index(driver, column_name):
    headers = get_table_headers(driver)
    for index, header in enumerate(headers, start=1):
        if column_name.lower() in header.lower():
            return index
    raise ValueError(f"Column '{column_name}' not found in table headers: {headers}")

def check_column_cells(driver, column_name):
    col_idx = get_column_index(driver, column_name)
    rows = driver.find_elements(*CommonTableLocators.TABLE_ROWS)
    return [row.find_element(By.XPATH, f"./td[{col_idx}]").text.strip() for row in rows]

def check_column_cells_not_empty(driver, column_name):
    col_idx = get_column_index(driver, column_name)
    cells = driver.find_elements(By.XPATH, f"//tbody/tr/td[{col_idx}]")
    if not cells:
        return False  # No rows present in the table
    for cell in cells:
        cell_text = cell.text.strip()
        # Check if blank, exact dash, or 1 character or fewer
        if not cell_text or cell_text == "-" or len(cell_text) <= 1:
            return False  # Invalid cell text found
    return True


def click_edit_btn(driver, target):
    if isinstance(target, int):
        wait_for_and_click(driver, *CommonTableLocators.EDIT_BTN_BY_INDEX(target))
    else:
        wait_for_and_click(driver, *CommonTableLocators.EDIT_BTN_BY_VALUE(str(target)))

def click_edit_btn_by_row_index(driver, row_idx=1):
    locator = CommonTableLocators.EDIT_BTN_BY_INDEX(row_idx)
    wait_for_and_click(driver, *locator)

def click_edit_btn_by_column_value(driver, column_name, text):
    col_idx = get_column_index(driver, column_name)
    locator = CommonTableLocators.EDIT_BTN_BY_COLUMN_VALUE(col_idx, text)
    wait_for_and_click(driver, *locator)

def search_in_table(driver, search_term):
    search_eneter = wait_and_type(driver, *SearchLocators.GLOBAL_SEARCH_INPUT, text=search_term)
    search_eneter.send_keys(Keys.ENTER)

def clear_input_field(driver, locator):
    element = driver.find_element(*locator)
    element.click()
    element.send_keys(Keys.CONTROL, "a")
    element.send_keys(Keys.BACKSPACE)

def select_custom_dropdown(driver, dropdown_label, option_text):
    wait_for_and_click(driver, *DropdownLocators.DROPDOWN_CONTAINER_BY_LABEL(dropdown_label))
    wait_for_and_click(driver, *DropdownLocators.DROPDOWN_OPTION(option_text))

def expand_tree_row(driver, row_index):
    wait_for_and_click(driver, *TreeTableLocators.EXPAND_CARET_BY_ROW(row_index))

def verify_no_results_found(driver, expected_text="No results found", timeout=5):
    try:
        table_body = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(CommonTableLocators.TABLE_BODY)
        )
        actual_text = table_body.text.strip()
        return expected_text.lower() in actual_text.lower()
    except Exception as e:
        print(f"[ERROR] Failed to locate or verify empty table body: {e}")
        return False

