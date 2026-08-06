import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Fiscal_Year_Page.locators import Buttons, Options
from helpers import login_helper, setup_browser

@pytest.mark.ui
def test_TC_FE_FISCAL_YEAR_004(setup_browser):
    """
    TC_FE_FISCAL_YEAR_004 (UI/UX)
    Verify all components on the Fiscal Year page match the design requirements.
    """
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    login_helper(driver)

    # 1. Page Title
    page_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Fiscal Year')] | //div[contains(@class, 'title') and contains(text(), 'Fiscal Year')]"))
    )
    assert page_title.is_displayed(), "Page title 'Fiscal Year' is not displayed."

    # 2. Add Fiscal Year Button
    add_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, Buttons.ADD_FISCAL_YEAR_BUTTON))
    )
    assert add_button.is_displayed(), "'Add Fiscal Year' button is not displayed."

    # 3. Status Label and Dropdown
    status_dropdown = wait.until(
        EC.visibility_of_element_located((By.XPATH, Options.STATUS_DROPDOWN))
    )
    assert status_dropdown.is_displayed(), "Status dropdown filter is not displayed."

    # 4. Search Bar
    search_bar = wait.until(
        EC.visibility_of_element_located((By.XPATH, Options.SEARCH_FIELD))
    )
    assert search_bar.is_displayed(), "Search bar input is not displayed."

    # 5. Table Columns Verification
    expected_text_columns = [
        "Fiscal Year",
        "FY Code",
        "Start Date",
        "End Date",
        "Date Created",
        "Date Updated",
        "Active"
    ]

    headers = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table//th")))
    actual_columns = [header.text.strip() for header in headers]

    # Verify total column count (should be 8 including Actions)
    assert len(headers) >= 8, f"Expected at least 8 table columns, found {len(headers)}"

    # Verify text columns
    for col in expected_text_columns:
        assert col in actual_columns, f"Expected column '{col}' was not found in table headers: {actual_columns}"
    
    
    # 6. Rows per page Label and Dropdown
    rows_per_page = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class = 'MuiTablePagination-selectLabel css-1chpzqh']"))
    )
    assert rows_per_page.is_displayed(), "'Rows per page' selector is not displayed."

    # 7. Pagination Controls
    pagination_container = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class = 'MuiTablePagination-displayedRows css-1chpzqh']"))
    )
    assert pagination_container.is_displayed(), "Pagination controls are not displayed."