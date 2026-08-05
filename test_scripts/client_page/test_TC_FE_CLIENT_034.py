from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_034(authenticated_driver):
    """
    (Functionality) Verify the Edit/Pencil button opens the "Update Client" modal:
    1. Click the Edit/Pencil button for a specific record.
    2. Verify the "Update Client" modal is displayed/visible.
    """
    driver= authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Click the Edit button for a specific record in the table
    TablePagination.change_rows_per_page(driver, 100)

    time.sleep(2)
    TableActions.click_edit_btn_by_column_value (driver, "Contact Person", "John Doe")
    # Step 2: Verify the Update Client modal pops up
    assert ComponentVerifier.is_component_visible(
        driver,
        Update_Modal_Inputs.MODAL_BODY
    ), "Expected 'Update Client' modal to pop up, but it was not visible!"

    driver.quit()