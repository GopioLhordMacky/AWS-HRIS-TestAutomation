from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_clients_005(client_page):
    """TC_FE_CLIENTS_005: Verify the '+ Add Client' button opens the 'Add Client' modal."""
    page = client_page

    # Step 1: Click the "+ Add Client" button
    page.click_add_client_button()

    # Step 2: Verify the "Add Client" modal pops up
    assert page.ensure_element_visible(
        Update_Modal_Inputs.MODAL_BODY
    ), "The 'Add Client' modal failed to pop up."