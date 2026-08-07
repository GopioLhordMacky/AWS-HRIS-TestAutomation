from pages.client_page import *
from locators.client_page_locators import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *
from utils.navigation_helpers import go_to_fiscal_year_page



def test_tc_fe_client_001(client_page):
    page = client_page
    go_to_fiscal_year_page(  via="url")
    time.sleep(2)

    


