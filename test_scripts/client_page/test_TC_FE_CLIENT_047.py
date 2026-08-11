from utils.navigation_helpers import go_to_client_page

class TestClientPage:
        
    def test_tc_fe_clients_047(self, authenticated_driver):
        """
        TC_FE_CLIENTS_048: Verify Column Sorting in Ascending Order (Client Page)
        
        1. Navigate to Client Page.
        2. Expand rows per page view to 100 to show max data entries.
        3. Click column header to trigger sort.
        4. Verify column contents display in ascending order.
        """
        page = go_to_client_page(authenticated_driver, via="url")

        column_to_sort = "Client Name"

        # Step 1: Change rows per page to 100
        page.change_rows_per_page_client(100)

        # Step 2 & 3: Trigger sort and verify ascending order
        page.verify_column_sorting_client(column_to_sort, order="ascending")

    