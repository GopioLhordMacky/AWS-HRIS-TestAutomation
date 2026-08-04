from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_024():
    """
    (Functionality) Verify Default Selected Value in Status Dropdown:
    1. The default selected value should be Active.
    2. The dropdown should not have a null or empty value selected by default.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    expected_default_value = "Active"

    # Step 1 & 2: Verify default value is 'Active' and neither empty nor null
    assert verify_input_matches(
        driver,
        locator=Filter_and_Search_Section.STATUS_FILTER_DROPDOWN,
        expected_text=expected_default_value
    ), f"Status dropdown default value did not match expected: '{expected_default_value}'"

    close_browser(driver)