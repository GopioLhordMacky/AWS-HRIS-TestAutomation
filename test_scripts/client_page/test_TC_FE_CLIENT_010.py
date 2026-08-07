from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_010(client_page):
    """TC_FE_CLIENTS_010: Verify Dropdown Loading Performance in '+ Add Client' Modal."""
    page = client_page


    # Step 1: Open Add Client Modal
    page.click_add_client_button()
    assert page.is_component_visible(  Update_Modal_Inputs.MODAL_BODY), "Modal failed to open."

    # Step 2: Measure Industry Dropdown Performance
    start_time = time.perf_counter()
    page.select_react_dropdown(  Update_Modal_Inputs.INDUSTRY_SELECT, ClientFormData.VALID_INDUSTRY)
    industry_duration = time.perf_counter() - start_time

    assert industry_duration < 3.0, f"Industry dropdown selection took too long: {industry_duration:.2f}s"

    # Step 3: Measure Country Dropdown Performance
    start_time = time.perf_counter()
    page.select_react_dropdown(  Update_Modal_Inputs.COUNTRY_SELECT, ClientFormData.VALID_COUNTRY)
    country_duration = time.perf_counter() - start_time

    assert country_duration < 3.0, f"Country dropdown selection took too long: {country_duration:.2f}s"

    