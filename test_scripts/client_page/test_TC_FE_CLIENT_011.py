from pages.client_page import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_011(driver):
    """Verify that adding a client with leading/trailing whitespace in fields successfully saves and displays in the table."""
    login_client_page(driver)

    # Generate dynamic client name
    client_name = ClientFormData.get_unique_client_name(prefix="TA")

    # Step 1: Open modal and fill form with whitespace inputs
    click_add_client_button(driver)
    fill_client_form(
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
    assert ComponentVerifier.check_table_data_by_search(driver, "Client Name", client_name), f"Client Name '{client_name}' not found in table."

    driver.quit()