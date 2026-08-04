from locators.shared.shared_locators import PaginationLocators
from helpers.main_helpers.setup_browser import wait_for_and_click, ensure_element_visible


def change_rows_per_page(driver, count):
    wait_for_and_click(driver, *PaginationLocators.ROWS_PER_PAGE_DROPDOWN)
    wait_for_and_click(driver, *PaginationLocators.ROWS_PER_PAGE_OPTION(count))

def go_to_next_page(driver):
    wait_for_and_click(driver, *PaginationLocators.NEXT_PAGE_BTN)

def go_to_prev_page(driver):
    wait_for_and_click(driver, *PaginationLocators.PREV_PAGE_BTN)

def get_pagination_information(driver):
    element = ensure_element_visible(driver, *PaginationLocators.PAGINATION_INFO_TEXT)
    return element.text.strip()

