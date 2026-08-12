from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from imports.main_imports import *
from pages.base_page import BasePage
from components.tables import Table
from components.elements import Element
from components.modals import Modals
from components.navigation import Navigation


class PaginationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver) 
        self.table = Table(driver)   
        self.element = Element(driver)           
        self.navigation = Navigation(driver)
        self.modal = Modals(driver)

    def find_next_button(self):
      return self.find_element(PaginationLocators.NEXT_PAGE_BTN)

    def find_prev_button(self):
        return self.find_element(PaginationLocators.PREV_PAGE_BTN)

    def is_row_per_page_dropdown_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.ROWS_PER_PAGE_DROPDOWN)

    def is_next_page_button_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.NEXT_PAGE_BTN)

    def is_next_prev_button_visible(self):
        return True and self.element.is_component_visible(PaginationLocators.PREV_PAGE_BTN)
    
    def tab_navigation_next_btn(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(PaginationLocators.NEXT_PAGE_BTN,
                                                [Keys.ENTER],
                                                        helper, *helper_args, **helper_kwargs)

    def tab_navigation_prev_btn(self, helper=None, *helper_args, **helper_kwargs):
        """Navigates via keyboard Tab key until focus reached."""
        return self.navigation.tab_navigation(PaginationLocators.PREV_PAGE_BTN,
                                                [Keys.SPACE],
                                                        helper, *helper_args, **helper_kwargs)
    def get_pagination_information(self):
        """Returns pagination text string (e.g. '1-10 of 50')."""
        return self.table.get_pagination_information()