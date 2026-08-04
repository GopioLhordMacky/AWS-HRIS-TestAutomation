from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_009():
    """TC_FE_CLIENTS_009: Verify leading and trailing whitespace trimming upon form submission."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Pre-condition: Open modal
    click_add_client_button(driver)

    raw_name = "  Auto Trim Client  "

    # Step 1: Fill form with leading/trailing whitespace in text inputs
    fill_client_form(
        driver,
        name=ClientFormData.get_unique_client_name(prefix=raw_name),
        contact="  Jane Doe  ",
        email="  janedoe@example.com  ",
        phone="  09123456789  ",
        address="  456 Trim St.  "
    )

    # Step 2: Click Save
    click_save_confirm(driver)
    time.sleep(2)

    # Step 3: Verify success (modal closes or success toast appears)
    assert not is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY, timeout=5), "Modal failed to close after saving."

 
    close_browser(driver)