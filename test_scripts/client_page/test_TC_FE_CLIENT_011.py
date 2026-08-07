from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_clients_011(client_page):
    """Verify that adding a client with leading/trailing whitespace in fields successfully saves and displays in the table."""
    page = client_page

    # # Generate dynamic client name
    client_name = ClientFormData.get_unique_client_name(prefix="Test Automate")

    # Step 1: Open modal and fill form with whitespace inputs
    page.click_add_client_button()
    page.fill_client_form(
         
        name=client_name,
        contact="  Jane Doe  ",
        email="  janedoe@example.com  ",
        phone="  09123456789  ",
        address="  456 Trim St.  "
    )

    # Step 2: Save and confirm entry
    page.click_save_confirm()
    time.sleep(2)

    # Step 3: Verify the new entry exists in the table using check_table_data
    assert page.check_table_data_by_search("Client Name", client_name), f"Client Name '{client_name}' not found in table."

    