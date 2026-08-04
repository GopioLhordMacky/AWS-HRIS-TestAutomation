from pages.client_page import *
 
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

@pytest.mark.passed
def test_tc_fe_clients_038():
    """
    (Functionality) Verify Pre-Selected Data in Update Client Textbox and 
    Dropdowns Matches Table Data.
    """
    driver = open_browser("chrome")
    login_client_page(driver)
    time.sleep(3)

    target_row_idx = 1  # 1-based index for row 1

    # Step 1: Scrape text directly using column headers instead of hardcoded array indices
    client_name_col = get_column_index(driver, "Client Name")
    industry_col = get_column_index(driver, "Industry")
    country_col = get_column_index(driver, "Country")
    contact_col = get_column_index(driver, "Contact Person")

    table_data = {
        "client_name": driver.find_element(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{client_name_col}]").text.strip(),
        "industry": driver.find_element(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{industry_col}]").text.strip(),
        "country": driver.find_element(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{country_col}]").text.strip(),
        "contact_person": driver.find_element(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{contact_col}]").text.strip(),
    }

    # Step 2: Open modal
    time.sleep(2)
    click_edit_btn_by_row_index(driver, row_idx=target_row_idx)
    time.sleep(2)


    # Step 3: Wait for modal to render
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Update_Modal_Inputs.MODAL_BODY)
    )

    # Step 4: Verify text inputs via .get_attribute("value")
    modal_client_name = driver.find_element(*Update_Modal_Inputs.CLIENT_NAME_INPUT).get_attribute("value").strip()
    modal_contact_person = driver.find_element(*Update_Modal_Inputs.CONTACT_PERSON_INPUT).get_attribute("value").strip()

    # Safely scrape React-Select values
    def get_dropdown_value(label_name):
        elems = driver.find_elements(
            By.XPATH, 
            f"//div[contains(@class, 'modal-content')]//label[text()='{label_name}']/following::div[contains(@class, '-singleValue')][1]"
        )
        return elems[0].text.strip() if elems else ""

    modal_industry = get_dropdown_value("Industry")
    modal_country = get_dropdown_value("Country")

    # Step 5: Assertions
    assert modal_client_name == table_data["client_name"], f"Client Name mismatch! Table: {table_data['client_name']} | Modal: {modal_client_name}"
    assert modal_contact_person == table_data["contact_person"], f"Contact Person mismatch! Table: {table_data['contact_person']} | Modal: {modal_contact_person}"
    assert modal_industry == table_data["industry"], f"Industry mismatch! Table: {table_data['industry']} | Modal: {modal_industry}"
    assert modal_country == table_data["country"], f"Country mismatch! Table: {table_data['country']} | Modal: {modal_country}"

    close_browser(driver)