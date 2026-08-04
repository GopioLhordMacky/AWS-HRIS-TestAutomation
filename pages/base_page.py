import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators.client_page_locators import *
from imports.main_imports.main_imports import *

class ElementActions:
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