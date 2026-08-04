import time
from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_36():
    """TC_FE_CLIENTS_010: Verify Dropdown Loading Performance in '+ Add Client' Modal."""
    driver = open_browser("chrome")
    login_client_page(driver)

    # Step 1: Open Add Client Modal
    click_edit_button(driver)
    assert ComponentVerifier.is_component_visible(driver, Update_Modal_Inputs.MODAL_BODY), "Modal failed to open."

    # Step 2: Measure Industry Dropdown Performance
    start_time = time.perf_counter()
    select_react_dropdown(driver, Update_Modal_Inputs.INDUSTRY_SELECT, ClientFormData.VALID_INDUSTRY)
    industry_duration = time.perf_counter() - start_time

    assert industry_duration < 3.0, f"Industry dropdown selection took too long: {industry_duration:.2f}s"

    # Step 3: Measure Country Dropdown Performance
    start_time = time.perf_counter()
    select_react_dropdown(driver, Update_Modal_Inputs.COUNTRY_SELECT, ClientFormData.VALID_COUNTRY)
    country_duration = time.perf_counter() - start_time

    assert country_duration < 3.0, f"Country dropdown selection took too long: {country_duration:.2f}s"

    close_browser(driver)