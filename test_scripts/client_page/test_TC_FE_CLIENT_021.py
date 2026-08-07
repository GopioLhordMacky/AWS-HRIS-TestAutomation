from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_021(client_page):
    """Verify that the Industry dropdown selection filters the data displayed in the table."""
    page = client_page


    target_dropdown = "Industry"
    target_industry = "Information Technology Services"

    # Step 1: Select "Automotive" from the Industry filter dropdown
    page.select_custom_dropdown(
         
        target_dropdown,
        target_industry
    )
    time.sleep(3)

    # Step 2: Verify that all table rows across all pages match the selected industry
    assert page.check_table_data_by_dropdown(
         
        target_dropdown,
        target_industry
    ), f"Expected all table records in 'Industry' column to contain '{target_industry}', but found mismatching records."

    