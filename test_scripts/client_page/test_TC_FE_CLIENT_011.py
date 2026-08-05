from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_011(authenticated_driver):
    """Verify that adding a client with leading/trailing whitespace in fields successfully saves and displays in the table."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Generate dynamic client name
    client_name = ClientFormData.get_unique_client_name(prefix="TA")

    # Step 1: Open modal and fill form with whitespace inputs
    ClientPage.click_add_client_button(driver)
    ClientPage.fill_client_form(
        driver,
        name=client_name,
        contact="  Jane Doe  ",
        email="  janedoe@example.com  ",
        phone="  09123456789  ",
        address="  456 Trim St.  "
    )

    # Step 2: Save and confirm entry
    ModalActions.click_save_confirm(driver)

    # Step 3: Verify the new entry exists in the table using check_table_data
    assert TableSearch.check_table_data_by_search(driver, "Client Name", client_name), f"Client Name '{client_name}' not found in table."

    driver.quit()