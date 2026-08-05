from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_client_page

@pytest.mark.passed
def test_tc_fe_clients_36(authenticated_driver):
    """TC_FE_CLIENTS_010: Verify Dropdown Loading Performance in '+ Add Client' Modal."""
    driver = authenticated_driver
    go_to_client_page(driver, via = "url")

    # Step 1: Open Add Client Modal
    ClientPage.click_edit_button(driver)
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal failed to open."

    # Step 2: Measure Industry Dropdown Performance
    start_time = time.perf_counter()
    # ClientPage.select_react_dropdown(driver, Update_Modal_Inputs.INDUSTRY_SELECT, ClientFormData.VALID_INDUSTRY)
    ModalActions.fill_edit_select_modal(driver, "Industry", ClientFormData.VALID_INDUSTRY)
    industry_duration = time.perf_counter() - start_time

    assert industry_duration < 3.0, f"Industry dropdown selection took too long: {industry_duration:.2f}s"

    # Step 3: Measure Country Dropdown Performance
    start_time = time.perf_counter()
    ModalActions.fill_edit_select_modal(driver, "Country", ClientFormData.VALID_COUNTRY)
    country_duration = time.perf_counter() - start_time

    assert country_duration < 3.0, f"Country dropdown selection took too long: {country_duration:.2f}s"

    driver.quit()