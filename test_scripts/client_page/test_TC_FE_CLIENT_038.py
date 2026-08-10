from utils.navigation_helpers import go_to_client_page
import time
from selenium.webdriver.common.by import By

class TestClientPage:
    def test_tc_fe_clients_038(self, authenticated_driver):
        """
        (Functionality) Verify Pre-Selected Data in Update Client Textbox and 
        Dropdowns Matches Table Data.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(3)

        target_row_idx = 1  # 1-based index for row 1

        # Step 1: Scrape text directly using column headers instead of hardcoded array indices
        client_name_col = page.get_column_index_client(  "Client Name")
        industry_col = page.get_column_index_client(  "Industry")
        country_col = page.get_column_index_client(  "Country")
        contact_col = page.get_column_index_client(  "Contact Person")

        table_data = {
            "client_name": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{client_name_col}]").text.strip(),
            "industry": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{industry_col}]").text.strip(),
            "country": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{country_col}]").text.strip(),
            "contact_person": page.find_elements(By.XPATH, f"//tbody/tr[{target_row_idx}]/td[{contact_col}]").text.strip(),
        }

        # Step 2: Open modal
        time.sleep(2)
        page.click_edit_btn_by_row_index_client()
        time.sleep(2)


        # Step 3: Wait for modal to render
        assert page.is_client_modal_visible_client(), "Client modal is not visible!"

        # Step 4: Verify text inputs via .get_attribute("value")
        modal_client_name = page.get_client_name()
        modal_contact_person = page.get_contact_person()

        modal_industry = page.get_dropdown_value("Industry")
        modal_country = page.get_dropdown_value("Country")
        time.sleep(2)

        # Step 5: Assertions
        assert modal_client_name == table_data["client_name"], f"Client Name mismatch! Table: {table_data['client_name']} | Modal: {modal_client_name}"
        assert modal_contact_person == table_data["contact_person"], f"Contact Person mismatch! Table: {table_data['contact_person']} | Modal: {modal_contact_person}"
        assert modal_industry == table_data["industry"], f"Industry mismatch! Table: {table_data['industry']} | Modal: {modal_industry}"
        assert modal_country == table_data["country"], f"Country mismatch! Table: {table_data['country']} | Modal: {modal_country}"

        