from selenium.webdriver.common.by import By
from locators.shared.shared_locators import ToggleSwitchLocators
from locators.shared.shared_locators import ViewModeLocators
from helpers.main_helpers.table_checkers import get_column_index
from helpers.main_helpers.setup_browser import wait_for_and_click

def toggle_active_status(driver, row_index, column_name="Active"):
    col_idx = get_column_index(driver, column_name)
    wait_for_and_click(driver, *ToggleSwitchLocators.TOGGLE_BY_ROW_AND_COL(row_index, col_idx))

def verify_active_toggle_state(driver, row_index, column_name="Active"):
    col_idx = get_column_index(driver, column_name)
    element = driver.find_element(*ToggleSwitchLocators.TOGGLE_BY_ROW_AND_COL(row_index, col_idx))
    return element.is_selected()

def switch_view_mode(driver, mode="table"):
    if mode.lower() == "table":
        wait_for_and_click(driver, *ViewModeLocators.TABLE_VIEW_BTN)
    elif mode.lower() == "card":
        wait_for_and_click(driver, *ViewModeLocators.CARD_VIEW_BTN)

def check_toggle_status_on_table(driver, column_name, text, timeout=10):
    """
    Dedicated helper for table columns that use switch/toggle controls 
    instead of plain text (e.g., Status/Active toggle columns).
    """
    try:
        headers = driver.find_elements(By.XPATH, "//table//th")
        col_index = -1
        for idx, header in enumerate(headers, start=1):
            if column_name.lower() in header.text.strip().lower():
                col_index = idx
                break
                
        if col_index == -1:
            print(f"[check_table_toggle_data_by_dropdown] Column '{column_name}' not found!")
            return False

        cells = driver.find_elements(By.XPATH, f"//table//tbody//tr/td[{col_index}]")
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