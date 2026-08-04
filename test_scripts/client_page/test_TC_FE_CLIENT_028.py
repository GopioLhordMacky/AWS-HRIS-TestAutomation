from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_028():
    """
    (Functionality) Verify that the table updates based on the search bar keyword
    across multiple columns (Client Name, Country, Contact Person).
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Define test data pairs: (search_keyword, target_column)
    search_test_cases = [
        ("test", "Client Name"),
        ("Philippines", "Country"),
        ("John Doe", "Contact Person")
    ]

    for search_keyword, target_column in search_test_cases:
        assert check_table_data_by_search(
            driver,
            column_name=target_column,
            text=search_keyword
        ), f"Search failed for keyword '{search_keyword}' under column '{target_column}'!"

    close_browser(driver)