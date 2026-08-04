from helpers.client_page_helpers import *
from helpers.main_helpers.check_components import *
from imports.main_imports.main_imports import *
from imports.client_page_imports import *

class TestClient001:

    @pytest.mark.passed
    def test_tc_fe_client_001(self):
        driver = open_browser("chrome")
        login_client_page(driver)
        time.sleep(2)
        
        assert is_client_page_loaded(driver), "Client page failed to load header or table."
        close_browser(driver)

if __name__ == "__main__":
    TestClient001().test_tc_fe_client_001()