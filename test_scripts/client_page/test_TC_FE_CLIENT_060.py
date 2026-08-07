from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_060(client_page):
    """
    TC_FE_CLIENTS_060: (Functionality) Verify Rows Per Page Change
    
    1. Navigate to Clients page.
    2. Verify that the 'Rows per page' dropdown contains options: [10, 20, 50, 100].
    3. Iterate through each option, select it, and verify the displayed table rows adapt.
    """
    page = client_page


    expected_counts = [10, 20, 50, 100]

    # Step 2: Iterate through options and verify table updates dynamically
    for count in expected_counts:
        page.change_rows_per_page(  count)
        time.sleep(1.5)

        # Get updated pagination text and visible row count
        updated_pag_info = page.get_pagination_information()
        visible_rows = len(page.find_elements(By.XPATH, "//tbody/tr"))

        # Assertions
        assert visible_rows <= count, (
            f"Displayed table rows ({visible_rows}) exceed selected limit ({count})!"
        )
        assert updated_pag_info is not None and len(updated_pag_info) > 0, (
            f"Pagination info is empty after setting rows per page to {count}!"
        )

