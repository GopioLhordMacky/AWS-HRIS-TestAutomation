from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_020(authenticated_driver):
    """Verify Default Selected Value in Industry Dropdown on Clients page."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")
    time.sleep(3)

    # Steps 1-4: Observe Industry dropdown default selection on the main Clients page table filter
    assert ComponentVerifier.verify_input_matches(
        driver,
        Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        "All"
    ), "Expected default selected value in Industry dropdown to be 'ALL', but it was not."

    driver.quit()