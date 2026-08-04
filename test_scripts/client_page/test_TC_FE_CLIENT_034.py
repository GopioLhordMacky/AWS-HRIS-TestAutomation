from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_034():
    """
    (Functionality) Verify the Edit/Pencil button opens the "Update Client" modal:
    1. Click the Edit/Pencil button for a specific record.
    2. Verify the "Update Client" modal is displayed/visible.
    """
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Click the Edit button for a specific record in the table
    change_rows_per_page(driver, 100)

    time.sleep(2)
    click_edit_btn_by_column_value (driver, "Contact Person", "John Doe")
    # Step 2: Verify the Update Client modal pops up
    assert ComponentVerifier.is_component_visible(
        driver,
        Update_Modal_Inputs.MODAL_BODY
    ), "Expected 'Update Client' modal to pop up, but it was not visible!"

    close_browser(driver)