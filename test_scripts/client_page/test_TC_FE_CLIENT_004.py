from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
import pytest
from selenium import webdriver
from utils.navigation_helpers import go_to_client_page


@pytest.mark.passed
def test_tc_fe_clients_004 (authenticated_driver):
    """Verify UI design and presence of mandatory components on Clients Module."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    time.sleep(2)

    #1. Title & Core Table
    assert ClientPage.is_client_page_loaded(driver), "Title or Table is missing."

    # 2. Add Client Button & Search Bar
    assert ComponentVerifier.is_component_clickable(driver, Client_Locators.ADD_CLIENT_BUTTON, timeout=10), "Add Client button missing."
    assert ComponentVerifier.is_component_visible(driver, Filter_and_Search_Section.SEARCH_BAR), "Search bar missing."

    # 3. Dropdowns (Industry, Status, Rows per page)
    assert ComponentVerifier.is_component_visible(driver, Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN), "Industry dropdown missing."
    assert ComponentVerifier.is_component_visible(driver, Filter_and_Search_Section.STATUS_FILTER_DROPDOWN), "Status dropdown missing."

    # 4. Table Columns Check
    headers = TableData.get_table_headers(driver)
    expected_columns = ["Client Name", "Industry", "Country", "Contact Person", "Active"]
    for column in expected_columns:
        assert any(column.lower() in h.lower() for h in headers), f"Column '{column}' missing from table."

    # 5. Pagination Component Check
    assert ComponentVerifier.is_component_visible(driver, Pagination_Section.PAGINATION_CONTAINER), "Pagination component missing."

    driver.close()