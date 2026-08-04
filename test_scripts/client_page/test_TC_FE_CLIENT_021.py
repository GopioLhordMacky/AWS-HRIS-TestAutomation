from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_021():
    """Verify that the Industry dropdown selection filters the data displayed in the table."""
    driver = open_browser("chrome")
    login_client_page(driver)

    target_dropdown = "Industry"
    target_industry = "Information Technology Services"

    # Step 1: Select "Automotive" from the Industry filter dropdown
    select_custom_dropdown(
        driver,
        target_dropdown,
        target_industry
    )
    time.sleep(3)

    # Step 2: Verify that all table rows across all pages match the selected industry
    assert check_table_data_by_dropdown(
        driver,
        target_dropdown,
        target_industry
    ), f"Expected all table records in 'Industry' column to contain '{target_industry}', but found mismatching records."
    close_browser(driver)