from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_024(client_page):
    """
    (Functionality) Verify Default Selected Value in Status Dropdown:
    1. The default selected value should be Active.
    2. The dropdown should not have a null or empty value selected by default.
    """
    page = client_page


    expected_default_value = "Active"

    # Step 1 & 2: Verify default value is 'Active' and neither empty nor null
    assert page.verify_input_matches(
         
        locator=Filter_and_Search_Section.STATUS_FILTER_DROPDOWN,
        expected_text=expected_default_value
    ), f"Status dropdown default value did not match expected: '{expected_default_value}'"

    