# ==========================================
# SELENIUM & DRIVER MODULES
# ==========================================
import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait, Select
import platform
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

# ==========================================
# SHARED LOCATORS
# ==========================================
from locators.shared.shared_locators import (
    LoginLocators,
    CommonTableLocators,
    SearchLocators,
    DropdownLocators,
    PaginationLocators,
    ToggleSwitchLocators,
    TabNavigationLocators,
    ViewModeLocators,
    TreeTableLocators,
    ModalLocators,
    ToastButtons
)

# ==========================================
# MAIN HELPER FUNCTIONS
# ==========================================
from helpers.main_helpers.setup_browser import (
    open_browser,
    close_browser,
    capture_screenshot,
    wait_for_and_click,
    wait_and_type,
    scroll_into_view,
    ensure_element_visible,
)

from helpers.main_helpers.login import (
    login,
    navigate_to_page,
    switch_tab,
)

from helpers.main_helpers.table_checkers import (
    get_table_headers,
    get_single_table_row_data,
    count_table_rows,
    get_column_index,
    get_table_row_data,
    check_column_cells,
    check_column_cells_not_empty,
    click_edit_btn,
    search_in_table,
    select_custom_dropdown,
    expand_tree_row,
    clear_input_field,
    verify_no_results_found,
    click_edit_btn_by_column_value,
    click_edit_btn_by_row_index,
)

from helpers.main_helpers.table_search import (
    check_table_data_by_search,
    check_table_data_by_dropdown,
    check_table_verify_no_results
)

from helpers.main_helpers.toggle_switch import (
    toggle_active_status,
    verify_active_toggle_state,
    switch_view_mode,
    check_toggle_status_on_table
)

from helpers.main_helpers.paginations import (
    change_rows_per_page,
    go_to_next_page,
    go_to_prev_page,
    get_pagination_information,
)

from helpers.main_helpers.check_components import (
    is_component_visible,
    is_component_clickable,
    verify_input_is_empty,
    verify_input_matches
)
from helpers.main_helpers.modal_components import (
    click_close,
    click_edit_btn,
    click_outside_modal,
    click_save_cancel,
    click_save_confirm,
    click_confirm,
    click_save_only,
    click_close_x,
    check_error_message,
    check_toast_message,
    fill_edit_select_modal,
    fill_edit_text_modal,

)

from helpers.main_helpers.tab_navigation import (
    tab_navigation
)

from helpers.main_helpers.table_sorting import (
    verify_column_sorting,
    sort_column
    )