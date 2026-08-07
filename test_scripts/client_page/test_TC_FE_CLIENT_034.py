from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_034(client_page):
    """
    (Functionality) Verify the Edit/Pencil button opens the "Update Client" modal:
    1. Click the Edit/Pencil button for a specific record.
    2. Verify the "Update Client" modal is displayed/visible.
    """
    page = client_page


    # Step 1: Click the Edit button for a specific record in the table
    page.change_rows_per_page(  100)

    time.sleep(2)
    page.click_edit_btn_by_column_value (  "Contact Person", "John Doe")
    # Step 2: Verify the Update Client modal pops up
    assert page.is_component_visible(
         
        Update_Modal_Inputs.MODAL_BODY
    ), "Expected 'Update Client' modal to pop up, but it was not visible!"

    