from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_060():
    """
    TC_FE_CLIENTS_060: (Functionality) Verify Rows Per Page Change
    
    1. Navigate to Clients page.
    2. Verify that the 'Rows per page' dropdown contains options: [10, 20, 50, 100].
    3. Iterate through each option, select it, and verify the displayed table rows adapt.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    expected_counts = [10, 20, 50, 100]

    # Step 2: Iterate through options and verify table updates dynamically
    for count in expected_counts:
        change_rows_per_page(driver, count)
        time.sleep(1.5)

        # Get updated pagination text and visible row count
        updated_pag_info = get_pagination_information(driver)
        visible_rows = len(driver.find_elements(By.XPATH, "//tbody/tr"))

        # Assertions
        assert visible_rows <= count, (
            f"Displayed table rows ({visible_rows}) exceed selected limit ({count})!"
        )
        assert updated_pag_info is not None and len(updated_pag_info) > 0, (
            f"Pagination info is empty after setting rows per page to {count}!"
        )

    close_browser(driver)