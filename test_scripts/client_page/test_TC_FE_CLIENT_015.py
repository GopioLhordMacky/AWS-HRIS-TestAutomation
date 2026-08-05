from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_015(authenticated_driver):
    """Verify Email Address Field Accepts Valid Email Format in Add Modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via="url")

    # Step 1: Open Add Client Modal
    ClientPage.click_add_client_button(driver)

    # Steps 2–4: Fill client form using the target valid email address
    ClientPage.fill_client_form(
        driver,
        email="client@email.com"
    )

    # Step 5: Click Save button to submit the form
    ModalActions.click_save_only(driver)

    # Verification: Ensure no validation error alert/message is triggered
    assert not ModalNotifications.check_error_message(driver), \
        "Expected valid email 'client@email.com' to be accepted, but validation error appeared."

    driver.quit()