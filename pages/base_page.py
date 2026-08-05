import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.config import IMPLICIT_WAIT
from locators.client_page_locators import *
from imports.main_imports.main_imports import *

class BasePage:
    """
    BasePage is a parent class for all page objects.
    It contains reusable methods like clicking, typing, waiting for elements,
    and checking element presence/visibility.
    """
    def __init__(self, driver):
        """
        Initialize with the Selenium WebDriver instance and set an explicit wait.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.timeout = 10 
        self.wait = WebDriverWait(driver, IMPLICIT_WAIT)

    def type(self, locator, text):
        """Finds an element and types text into it."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """Finds an element and clicks it."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @staticmethod
    def wait_for_and_click(driver, by, value, timeout=10):
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
        return element

    @staticmethod
    def wait_and_type(driver, by, value, text, timeout=10):
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)
        return element

    @staticmethod
    def scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def ensure_element_visible(driver, element, timeout=10):
        WebDriverWait(driver, timeout).until(EC.visibility_of(element))
        return element

    @staticmethod
    def clear_input_field(driver, locator):
        element = driver.find_element(*locator)
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)