from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_050(self, authenticated_driver):
        """
        TC_FE_CLIENTS_049: (Functionality) Verify Industry values are displayed correctly.
        
        1. Navigate to Clients page.
        2. Change rows per page to 100.
        3. Verify all Industry cells on current page have valid text.
        4. Paginate using go_to_next_page until the next button becomes disabled.
        """
        ## THIS WILL FAIL BECAUSE SOME COUNTRY CELLS ARE EMPTY. NEED TO FIX DATA IN DB OR ADD A CHECK FOR EMPTY CELLS. ## 
        page = go_to_client_page(authenticated_driver, via="url")

        target_column = "Country"

        # Step 1: Maximize rows displayed
        page.change_rows_per_page_client(100)
        time.sleep(1)

        # Step 2: Loop through pages
        while True:
            # 1. Assert current page column data is valid
            assert page.check_column_cells_not_empty_client(target_column), (
                f"Found empty or missing '{target_column}' value on the current page!"
            )

            # 2. Find the Next page button element
            next_btn = page.find_next_button()

            # 3. Check if button is disabled/inactive BEFORE clicking
            if not next_btn:
                break
                
            is_disabled_attr = "disabled" in (next_btn.get_attribute("class") or "")
            is_disabled_prop = not next_btn.is_enabled() or next_btn.get_attribute("disabled") is not None

            if is_disabled_attr or is_disabled_prop:
                print("Reached the last page. Pagination complete.")
                break

            # 4. Advance to the next page ONCE using your helper method
            page.go_to_next_page_client()
            time.sleep(2)  # Wait for table DOM to re-render