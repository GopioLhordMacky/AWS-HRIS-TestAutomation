from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_031():
    """
    (Functionality) Verify Search Bar Handles Partial Matches:
    1. Enter a partial string of a valid Client Name, Industry, Country, or Contact Person.
    2. Verify all rows containing the partial string are displayed correctly.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Test cases: (partial_search_term, target_column)
    partial_match_cases = [
        ("Macky", "Client Name"),
        ("Philipp", "Country")
    ]

    for partial_term, target_column in partial_match_cases:
        assert check_table_data_by_search(
            driver,
            column_name=target_column,
            text=partial_term
        ), f"Partial search failed for term '{partial_term}' under column '{target_column}'!"

    close_browser(driver)