from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_031(client_page):
    """
    (Functionality) Verify Search Bar Handles Partial Matches:
    1. Enter a partial string of a valid Client Name, Industry, Country, or Contact Person.
    2. Verify all rows containing the partial string are displayed correctly.
    """
    page = client_page

    # Test cases: (partial_search_term, target_column)
    partial_match_cases = [
        ("Macky", "Client Name"),
        ("Philipp", "Country")
    ]

    for partial_term, target_column in partial_match_cases:
        assert page.check_table_data_by_search(
             
            column_name=target_column,
            text=partial_term
        ), f"Partial search failed for term '{partial_term}' under column '{target_column}'!"

    