from locators.shared.shared_locators import CommonTableLocators
from helpers.main_helpers.paginations import *
from imports.main_imports.main_imports import *

def check_table_data_by_search(driver, column_name, text):
    """Filters the table using the search bar, expands rows per page to 100, 
    and verifies if the query text exists in the specified column.
    
    :param driver: WebDriver instance
    :param column_name: The header text of the target column
    :param text: The search query text expected in the cell
    :return: bool (True if text is found in column, False otherwise)
    """
    try:
        # 1. Refresh page at the start
        driver.refresh()
        time.sleep(1)

        # 2. Set rows per page to 100 to ensure all filtered results are visible
        change_rows_per_page(driver, 100)
        time.sleep(2)

        # 3. Filter the table using the built-in search input
        search_in_table(driver, text)
        time.sleep(3)  # Brief wait for table results to filter

        # 4. Get column index and row data
        col_idx = get_column_index(driver, column_name)
        col_list_idx = col_idx - 1
        table_data = get_table_row_data(driver)

        # 5. Check if target text exists in the specific column
        for row in table_data:
            if len(row) > col_list_idx:
                if text.lower() in row[col_list_idx].lower():
                    return True

        return False

    except Exception as e:
        print(f"[check_table_data] Error during table search check: {e}")
        return False

def check_table_data_by_dropdown(driver, column_name, text, timeout=10):
    """
    Filters the table using a dropdown filter, sets rows per page to 100, 
    and verifies across ALL pagination pages that EVERY row in the specified 
    column EXACTLY matches the target text (case-insensitive, trimmed).
    """
    try:
        # 1. Expand rows per page to 100
        change_rows_per_page(driver, 20)
        
        # Explicit wait for table rows to reload after changing rows per page
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(CommonTableLocators.TABLE_ROWS)
        )
        time.sleep(2)

        # 2. Filter the table using the dropdown
        select_custom_dropdown(driver, column_name, text)
        time.sleep(3)  # Wait for filter application

        expected_text = text.strip().lower()
        page_number = 1

        # Get column index
        col_idx = get_column_index(driver, column_name)
        col_list_idx = col_idx - 1

        # 3. Pagination loop
        while True:
            # Capture initial row reference to monitor page transition staleness
            current_row_elements = driver.find_elements(*CommonTableLocators.TABLE_ROWS)
            first_row_before = current_row_elements[0] if current_row_elements else None

            # Get row text data
            table_data = get_table_row_data(driver)

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
                has_next = go_to_next_page(driver)
            except Exception as e:
                print(f"[check_table_data] go_to_next_page returned exception/False: {e}")
                has_next = False

            if not has_next:
                print(f"[check_table_data] Reached end of pagination at page {page_number}.")
                break

            # If moving to next page, wait for old page's first row to go stale before re-checking
            if first_row_before:
                try:
                    WebDriverWait(driver, timeout).until(EC.staleness_of(first_row_before))
                except Exception:
                    time.sleep(2)

            page_number += 1

        return True

    except Exception as e:
        print(f"[check_table_data] Error during table search check: {e}")
        return False

def check_table_verify_no_results(driver, search_term, expected_text="No results found", timeout=5):



    """
    Searches for a term in the table and immediately verifies that no results are found.
    
    :param driver: WebDriver instance
    :param search_term: The invalid search term to enter
    :param expected_text: Text expected in the table body (default: 'No results found')
    :param timeout: Seconds to wait for element visibility
    :return: True if the search yields the expected empty state, False otherwise
    """
    # Step 1: Perform the search
    search_enter = wait_and_type(driver, *SearchLocators.GLOBAL_SEARCH_INPUT, text=search_term)
    search_enter.send_keys(Keys.ENTER)
    time.sleep(2)
    
    # Step 2: Verify the empty state in the table body
    try:
        table_body = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(CommonTableLocators.TABLE_BODY)
        )
        actual_text = table_body.text.strip()
        return expected_text.lower() in actual_text.lower()
    except Exception as e:
        print(f"[ERROR] Failed to locate or verify empty table body: {e}")
        return False