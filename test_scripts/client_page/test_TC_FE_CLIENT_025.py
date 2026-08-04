from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.skip(reason="Client Page has errors. Toggle Switch both has 'checked' attribute")
def test_tc_fe_clients_025():
    """
    (Functionality) Verify Status Selection Filters Data in Table:
    1. Select 'Active' from the Status dropdown and observe table records.
    2. Select 'Inactive' from the Status dropdown and observe table records.
    3. Ensure table only displays records matching the selected status, hiding unselected ones.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1 & 2: Select "Active" and verify table filters to Active records only
    active_option = "Active"
    select_custom_dropdown(driver, dropdown_label="Status", option_text=active_option)

    assert check_toggle_status_on_table(
        driver,
        column_name="Active",
        text=active_option
    ), f"Table failed to filter and display only '{active_option}' records."

    # Step 3 & 4: Select "Inactive" and verify table updates to Inactive records only
    inactive_option = "Inactive"
    select_custom_dropdown(driver, dropdown_label="Status", option_text=inactive_option)

    assert check_toggle_status_on_table(
        driver,
        column_name="Active",
        text=inactive_option
    ), f"Table failed to filter and display only '{inactive_option}' records."

    close_browser(driver)