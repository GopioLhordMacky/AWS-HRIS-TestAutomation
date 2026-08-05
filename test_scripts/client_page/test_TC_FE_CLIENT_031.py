from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_031(authenticated_driver):
    """
    (Functionality) Verify Search Bar Handles Partial Matches:
    1. Enter a partial string of a valid Client Name, Industry, Country, or Contact Person.
    2. Verify all rows containing the partial string are displayed correctly.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via = "url")

    # Test cases: (partial_search_term, target_column)
    partial_match_cases = [
        ("Macky", "Client Name"),
        ("Philipp", "Country")
    ]

    for partial_term, target_column in partial_match_cases:
        assert TableSearch.check_table_data_by_search(
            driver,
            column_name=target_column,
            text=partial_term
        ), f"Partial search failed for term '{partial_term}' under column '{target_column}'!"

    driver.quit()