from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_020(driver):
    """Verify Default Selected Value in Industry Dropdown on Clients page."""
    login_client_page(driver)
    time.sleep(3)

    # Steps 1-4: Observe Industry dropdown default selection on the main Clients page table filter
    assert ComponentVerifier.verify_input_matches(
        driver,
        Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        "All"
    ), "Expected default selected value in Industry dropdown to be 'ALL', but it was not."

    driver.quit()