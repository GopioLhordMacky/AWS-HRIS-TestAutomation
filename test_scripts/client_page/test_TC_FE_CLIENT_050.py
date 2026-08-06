from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_050(authenticated_driver):
    """
    TC_FE_CLIENTS_050: (Functionality) Verify Country values are displayed correctly.
    
    1. Navigate to Clients page.
    2. Change rows per page to 100.
    3. Verify all Country cells on current page have valid text.
    4. Paginate using go_to_next_page until the next button becomes disabled.
    """
    ## THIS WILL FAIL BECAUSE SOME COUNTRY CELLS ARE EMPTY. NEED TO FIX DATA IN DB OR ADD A CHECK FOR EMPTY CELLS. ## 
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    target_column = "Country"

    # Step 1: Maximize rows displayed
    TablePagination.change_rows_per_page(driver, 100)
    time.sleep(1)

    # Step 2: Loop through pages
    while True:
        # Check that all cells under 'Client Name' on the current page contain text
        assert TableData.check_column_cells_not_empty(driver, target_column), (
            f"Found empty or missing '{target_column}' value on the current page!"
        )

        # Check if Next button exists and is active/enabled before clicking
        next_btn = driver.find_elements(*PaginationLocators.NEXT_PAGE_BTN)
        
        # Break loop if button is missing, disabled, or contains 'disabled' in class
        if not next_btn or not next_btn[0].is_enabled() or "disabled" in next_btn[0].get_attribute("class"):
            break

        # Step 3: Advance to next page using helper
        TablePagination.go_to_next_page(driver)
        time.sleep(3)
        driver.quit()