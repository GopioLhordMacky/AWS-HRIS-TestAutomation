from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_028(client_page):
    """
    (Functionality) Verify that the table updates based on the search bar keyword
    across multiple columns (Client Name, Country, Contact Person).
    """
    page = client_page


    # Define test data pairs: (search_keyword, target_column)
    search_test_cases = [
        ("test", "Client Name"),
        ("Philippines", "Country"),
        ("John Doe", "Contact Person")
    ]

    for search_keyword, target_column in search_test_cases:
        assert page.check_table_data_by_search(
             
            column_name=target_column,
            text=search_keyword
        ), f"Search failed for keyword '{search_keyword}' under column '{target_column}'!"

    