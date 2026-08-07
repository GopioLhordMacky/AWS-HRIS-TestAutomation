from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_022(client_page):
    """
    (Accessibility) Verify that Industry dropdown can be navigated 
    and activated using keyboard.
    """
    page = client_page


    target_industry = "Automotive"

    # Step 1: Navigate to the Industry Dropdown via TAB
    # Step 2-4: Send ENTER (open menu) -> ARROW_DOWN (highlight Automotive) -> ENTER (select)
    keystroke_sequence = [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER]

    assert page.tab_navigation(
         
        locator=Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        keys=keystroke_sequence
    ), "Failed to navigate to Industry dropdown using TAB key."

    # Step 5: Verify that selected option correctly updates and reflects in the table across all pages
    assert page.check_table_data_by_dropdown(
         
        column_name="Industry",
        text=target_industry
    ), f"Expected table to filter for '{target_industry}' via keyboard navigation, but table check failed."

    



    