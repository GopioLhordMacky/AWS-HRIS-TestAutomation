from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

def test_tc_fe_client_002(client_page):
    """Verify Table Headers presence and structure on Client Page."""
    page = client_page
    time.sleep(1)
    headers = page.get_table_headers()
    # print(f"Captured Headers: {headers}")
    assert len(headers) > 0, "No headers were retrieved from the Client table."
    
