from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_030(client_page):
    """
    (Functionality) Verify Search is Case-Insensitive:
    1. Enter search keywords in various cases (uppercase, lowercase, mixed case).
    2. Verify search returns valid records for each case variation.
    3. Assert pagination info matches across all case variations.
    """
    page = client_page


    case_variations = ["teSt", "TEst", "tesT", "TEST", "tESt"]
    target_column = "Client Name"
    baseline_pagination = None

    for search_term in case_variations:
        # Step 1: Clear previous search input
        page.clear_input_field(  Filter_and_Search_Section.SEARCH_BAR)

        # Step 2: Search and validate data in table
        assert page.check_table_data_by_search(
             
            column_name=target_column,
            text=search_term
        ), f"Case-insensitivity search failed for keyword '{search_term}'!"

        time.sleep(1)
        current_pagination = page.get_pagination_information()

        # Step 3: Establish baseline from first search and compare all subsequent searches
        if baseline_pagination is None:
            baseline_pagination = current_pagination
        else:
            assert current_pagination == baseline_pagination, (
                f"Pagination mismatch for case variation '{search_term}'! "
                f"Expected: {baseline_pagination}, Got: {current_pagination}"
            )

    