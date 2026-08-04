from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_022(driver):
    """
    (Accessibility) Verify that Industry dropdown can be navigated 
    and activated using keyboard.
    """
    login_client_page(driver)

    target_industry = "Automotive"

    # Step 1: Navigate to the Industry Dropdown via TAB
    # Step 2-4: Send ENTER (open menu) -> ARROW_DOWN (highlight Automotive) -> ENTER (select)
    keystroke_sequence = [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER]

    assert KeyboardNavigation.tab_navigation(
        driver,
        locator=Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        keys=keystroke_sequence
    ), "Failed to navigate to Industry dropdown using TAB key."

    # Step 5: Verify that selected option correctly updates and reflects in the table across all pages
    assert TableSearch.check_table_data_by_dropdown(
        driver,
        column_name="Industry",
        text=target_industry
    ), f"Expected table to filter for '{target_industry}' via keyboard navigation, but table check failed."

    driver.quit()