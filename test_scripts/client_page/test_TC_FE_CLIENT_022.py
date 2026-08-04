from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_022():
    """
    (Accessibility) Verify that Industry dropdown can be navigated 
    and activated using keyboard.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    target_industry = "Automotive"

    # Step 1: Navigate to the Industry Dropdown via TAB
    # Step 2-4: Send ENTER (open menu) -> ARROW_DOWN (highlight Automotive) -> ENTER (select)
    keystroke_sequence = [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER]

    navigation_success = tab_navigation(
        driver,
        locator=Filter_and_Search_Section.INDUSTRY_FILTER_DROPDOWN,
        keys=keystroke_sequence
    )

    assert navigation_success, "Failed to navigate to Industry dropdown using TAB key."

    # Step 5: Verify that selected option correctly updates and reflects in the table across all pages
    assert check_table_data_by_dropdown(
        driver,
        column_name="Industry",
        text=target_industry
    ), f"Expected table to filter for '{target_industry}' via keyboard navigation, but table check failed."

    close_browser(driver)