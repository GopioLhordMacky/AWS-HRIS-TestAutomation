import time
import pytest
from utils.navigation_helpers import go_to_location_page
from data.location_page_inputs import (
    VALID_PROVINCE_INPUT,
    VALID_CITY_INPUT,
    HIERARCHY_TEST_CHAIN
)

class TestFLocationPage:

    def test_tc_fe_location_001_expand_tree_rows(self, authenticated_driver):
        """Verify expanding parent rows displays child nodes in the table."""
        page = go_to_location_page(authenticated_driver, via="url")
        
        # Get initial row count
        initial_count = page.get_location_table_row_count()
        
        # Expand row 1 tree (e.g., Country node)
        page.expand_row_tree_location(row_index=1)
        time.sleep(1)

        # Verify row count increased after expansion
        expanded_count = page.get_location_table_row_count()
        assert expanded_count > initial_count, (
            f"Expected table row count to increase after expanding tree, "
            f"but went from {initial_count} to {expanded_count}."
        )

    def test_tc_fe_location_002_add_country(self, authenticated_driver):
        """Verify typing and selecting a country in the React-Select dropdown."""
        page = go_to_location_page(authenticated_driver, via="url")
        
        page.open_add_country_modal()
        assert page.is_country_modal_visible(), "Add Country modal inputs are not visible."

        country_name = HIERARCHY_TEST_CHAIN["country"]
        page.fill_country(country_name)
        time.sleep(1)

        # Verify auto-populated read-only ISO Code field
        iso_code = page.get_auto_iso_code()
        assert iso_code != "" and iso_code is not None, f"ISO code failed to auto-populate for {country_name}."

        page.click_save_only_modal_location()
        time.sleep(2)

    def test_tc_fe_location_003_add_province(self, authenticated_driver):
        """Verify typing and selecting a province in the React-Select dropdown."""
        page = go_to_location_page(authenticated_driver, via="url")

        page.open_add_province_modal()
        assert page.is_province_modal_visible(), "Add Province modal inputs are not visible."

        province_name = VALID_PROVINCE_INPUT["province_name"]
        page.fill_province(province_name)
        time.sleep(1)

        # Verify auto-populated read-only State Code field
        state_code = page.get_auto_state_code()
        assert state_code != "" and state_code is not None, f"State code failed to auto-populate for {province_name}."

        page.click_save_only_modal_location()
        time.sleep(2)

    def test_tc_fe_location_004_add_city(self, authenticated_driver):
        """Verify typing and selecting a city in the React-Select dropdown."""
        page = go_to_location_page(authenticated_driver, via="url")

        page.open_add_city_modal()
        assert page.is_city_modal_visible(), "Add City modal inputs are not visible."

        city_name = VALID_CITY_INPUT["city_name"]
        page.fill_city(city_name)
        time.sleep(1)

        page.click_save_only_modal_location()
        time.sleep(2)