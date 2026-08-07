from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_049(client_page):
    """
    TC_FE_CLIENTS_049: (Functionality) Verify Industry values are displayed correctly.
    
    1. Navigate to Clients page.
    2. Change rows per page to 100.
    3. Verify all Industry cells on current page have valid text.
    4. Paginate using go_to_next_page until the next button becomes disabled.
    """
    ## THIS WILL FAIL BECAUSE SOME INDUSTRY CELLS ARE EMPTY. NEED TO FIX DATA IN DB OR ADD A CHECK FOR EMPTY CELLS. ## 
    page = client_page


    target_column = "Industry"

    # Step 1: Maximize rows displayed
    page.change_rows_per_page(  100)
    time.sleep(1)

    # Step 2: Loop through pages
    while True:
        # Check that all cells under 'Client Name' on the current page contain text
        assert page.check_column_cells_not_empty(  target_column), (
            f"Found empty or missing '{target_column}' value on the current page!"
        )

        # Check if Next button exists and is active/enabled before clicking
        next_btn = page.find_element(PaginationLocators.NEXT_PAGE_BTN).click()
        
        # Break loop if button is missing, disabled, or contains 'disabled' in class
        if not next_btn or not next_btn[0].is_enabled() or "disabled" in next_btn[0].get_attribute("class"):
            break

        # Step 3: Advance to next page using helper
        page.go_to_next_page()
        time.sleep(3)
