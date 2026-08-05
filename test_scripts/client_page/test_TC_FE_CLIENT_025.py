from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")
def test_tc_fe_clients_025(authenticated_driver):
    """
    (Functionality) Verify Status Selection Filters Data in Table:
    1. Select 'Active' from the Status dropdown and observe table records.
    2. Select 'Inactive' from the Status dropdown and observe table records.
    3. Ensure table only displays records matching the selected status, hiding unselected ones.
    """
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1 & 2: Select "Active" and verify table filters to Active records only
    active_option = "Active"
    FormControls.select_custom_dropdown(driver, dropdown_label="Status", option_text=active_option)

    assert TableActions.check_toggle_status_on_table(
        driver,
        column_name="Active",
        text=active_option
    ), f"Table failed to filter and display only '{active_option}' records."

    # Step 3 & 4: Select "Inactive" and verify table updates to Inactive records only
    inactive_option = "Inactive"
    FormControls.select_custom_dropdown(driver, dropdown_label="Status", option_text=inactive_option)

    assert TableActions.check_toggle_status_on_table(
        driver,
        column_name="Active",
        text=inactive_option
    ), f"Table failed to filter and display only '{inactive_option}' records."

    driver.quit()