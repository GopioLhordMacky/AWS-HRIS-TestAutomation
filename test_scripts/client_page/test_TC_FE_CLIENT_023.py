from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_023(client_page):
    """
    (Functionality) Verify the Status dropdown displays the correct list of options 
    ('Active', 'Inactive') and can select an option.
    """
    page = client_page



    expected_status_options = Options.status_options
    time.sleep(3)

    # Step 1 & 2: Verify that the Status dropdown displays the correct list of options
    assert page.verify_dropdown_options(
         
        dropdown_locator=Filter_and_Search_Section.STATUS_FILTER_DROPDOWN,
        expected_options=expected_status_options
    ), f"Status dropdown options did not match expected: {expected_status_options}"

    # Step 3: Select 'Active' from dropdown and verify filtering on toggle column
    target_option = "Active"
    page.select_custom_dropdown(  dropdown_label="Status", option_text=target_option)
    time.sleep(3)

    # Validate that the selected option filters the table properly
    ## THIS IS NOT WORKING, SINCE BOTH ACTIVE AND INACTIVE HAS 'checked' ATTRIBUTE ##
    assert page.check_toggle_status_on_table(
         
        column_name="Active",
        text=target_option
    ), f"Table did not properly update to reflect selected Status option: '{target_option}'"

    time.sleep(3)
    