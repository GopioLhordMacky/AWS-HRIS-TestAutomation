from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_027(authenticated_driver):
    """
    (Accessibility) Verify Search Bar Accepts Input:
    1. Click into the search bar.
    2. Type alphanumeric characters, special characters, and spaces.
    3. Verify search bar accepts and displays all typed characters correctly.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Mixed test string containing alphanumerics, spaces, and special characters
    test_search_input = "Test Client 123!@#"

    # Step 1 & 2: Focus search bar and type test input
    TableSearch.search_in_table(driver, test_search_input)

    # Step 3: Verify the search bar displays the typed string correctly
    assert verify_input_matches(
        driver,
        locator=Filter_and_Search_Section.SEARCH_BAR,
        expected_text=test_search_input
    ), f"Search bar input mismatch! Expected: '{test_search_input}'"

    close_browser(driver)