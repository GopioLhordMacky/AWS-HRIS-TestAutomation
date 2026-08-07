from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *



def test_tc_fe_clients_042(client_page):
    """
    TC_FE_CLIENTS_042: (Functionality) Verify Unsaved Changes Are Discarded When Pressing ESC
    
    1. Scrape initial table row data for reference (Client Name, Industry, Country, Contact Person).
    2. Open "Update Client" modal for the target row.
    3. Modify fields with new valid data.
    4. Click "ESC" without clicking "Save".
    5. Reopen "Update Client" modal for the exact same row.
    6. Verify that modal pre-selected data matches original table values, discarding changes.
    """
    page = client_page

    time.sleep(2)  
    target_row_idx = 3  # 1-based index for row 1

    # Step 1: Store initial table row values for counterchecking
    client_name_col = page.get_column_index(  "Client Name")
    industry_col = page.get_column_index(  "Industry")
    country_col = page.get_column_index(  "Country")
    contact_col = page.get_column_index(  "Contact Person")

    initial_table_data = {
        "client_name": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{client_name_col}]").text.strip(),
        "industry": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{industry_col}]").text.strip(),
        "country": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{country_col}]").text.strip(),
        "contact_person": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{contact_col}]").text.strip(),
    }

    # Step 2: Open "Update Client" modal
    page.click_edit_btn_by_row_index(  row_idx=target_row_idx)

    # Step 3: Modify form fields with unsaved changes
    page.update_client_form()

    # Step 4: Close modal without saving changes
    page.click_outside_modal()

    # Step 5: Reopen the "Update Client" modal for the exact same record
    page.click_edit_btn_by_row_index(  row_idx=target_row_idx)

    page.wait.until(
        EC.visibility_of_element_located(Update_Modal_Inputs.MODAL_BODY)
    )

    # Step 6: Scrape reopened modal values
    reopened_client_name = page.find_element(Update_Modal_Inputs.CLIENT_NAME_INPUT).get_attribute("value").strip()
    reopened_contact_person = page.find_element(Update_Modal_Inputs.CONTACT_PERSON_INPUT).get_attribute("value").strip()

    # def get_dropdown_value(label_name):
    #     elems = page.find_elements(
    #         By.XPATH, 
    #         f"//div[contains(@class, 'modal-content')]//label[text()='{label_name}']/following::div[contains(@class, '-singleValue')][1]"
    #     )
    #     return elems[0].text.strip() if elems else ""

    reopened_industry = page.get_dropdown_value("Industry")
    reopened_country = page.get_dropdown_value("Country")

    # Step 7: Assertions - Ensure values match initial state (changes discarded)
    assert reopened_client_name == initial_table_data["client_name"], (
        f"FAILED: Client Name modified after close! Expected: '{initial_table_data['client_name']}', Found: '{reopened_client_name}'"
    )
    assert reopened_contact_person == initial_table_data["contact_person"], (
        f"FAILED: Contact Person modified after close! Expected: '{initial_table_data['contact_person']}', Found: '{reopened_contact_person}'"
    )
    assert reopened_industry == initial_table_data["industry"], (
        f"FAILED: Industry modified after close! Expected: '{initial_table_data['industry']}', Found: '{reopened_industry}'"
    )
    assert reopened_country == initial_table_data["country"], (
        f"FAILED: Country modified after close! Expected: '{initial_table_data['country']}', Found: '{reopened_country}'"
    )

    