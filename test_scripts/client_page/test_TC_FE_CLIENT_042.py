from utils.navigation_helpers import go_to_client_page
import time

class TestClientPage:

    def test_tc_fe_clients_042(self, authenticated_driver):
        """
        TC_FE_CLIENTS_042: (Functionality) Verify Unsaved Changes Are Discarded When Pressing ESC
        1. Scrape initial table row data for reference (Client Name, Industry, Country, Contact Person).
        2. Open "Update Client" modal for the target row.
        3. Modify fields with new valid data.
        4. Click "ESC" without clicking "Save".
        5. Reopen "Update Client" modal for the exact same row.
        6. Verify that modal pre-selected data matches original table values, discarding changes.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        time.sleep(2)  
        # # Step 1: Store initial table row value
        initial_table_data = {
            "client_name": page.get_initial_client_name(),
            "industry": page.get_initial_industry(),
            "country": page.get_initial_country(),
            "contact_person": page.get_initial_contact_person(),
        }

        # Step 2: Open "Update Client" modal
        page.click_edit_btn_by_row_index_client()

        # Step 3: Modify form fields with unsaved changes
        page.update_client_form()

        # Step 4: Close modal without saving changes
        page.click_outside_modal_client()

        # Step 5: Reopen the "Update Client" modal for the exact same record
        page.click_edit_btn_by_row_index_client()

        # Step 6: Scrape reopened modal values
        reopened_client_name = page.get_client_name()
        reopened_contact_person = page.get_contact_person()
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

        