from locators.shared.shared_locators import CommonTableLocators
from helpers.main_helpers.paginations import *
from imports.main_imports.main_imports import *

def verify_column_sorting(driver, column_name, order="ascending", is_numeric=False):

    """
    Sorts a table column using `sort_column` and verifies that the column values
    are sorted in the expected order ('ascending' or 'descending').
    """
    # 1. Trigger the sort action
    sort_column(driver, column_name)
    time.sleep(1)  # Allow DOM/table re-render

    # 2. Get column index dynamically to locate the cells
    col_idx = get_column_index(driver, column_name)

    # 3. Collect all cell values for that column
    cells = driver.find_elements(By.XPATH, f"//tbody/tr/td[{col_idx}]")
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

def sort_column(driver, column_name):
    wait_for_and_click(driver, *CommonTableLocators.HEADER_BY_NAME(column_name))