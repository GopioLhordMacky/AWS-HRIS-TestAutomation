from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_026(authenticated_driver):
    """
    (Accessibility) Verify that Status dropdown can be navigated 
    and activated using keyboard.
    1. Focus Status dropdown via keyboard navigation.
    2. Press keys (Arrow Down, Enter) to select 'Inactive'.
    3. Verify that selected option updates correctly and reflects in table toggles.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1-4: Focus Status dropdown, navigate down to 'Inactive', and press ENTER
    target_status = "Inactive"
    dropdown_locator = Filter_and_Search_Section.STATUS_FILTER_DROPDOWN

    KeyboardNavigation.tab_navigation(
        driver,
        locator=dropdown_locator,
        keys=[Keys.ARROW_DOWN, Keys.ENTER]
    )

    # Step 5: Verify table updates to display 'Inactive' toggles
    assert TableActions.check_toggle_status_on_table(
        driver,
        column_name="Active",
        text=target_status
    ), f"Keyboard selection failed! Table did not update to reflect '{target_status}' records."

    driver.quit()