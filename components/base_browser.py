import os
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imports.main_imports.main_imports import *

class BrowserSetup():

    @staticmethod
    def open_browser(browser_name="chrome"):
        if browser_name.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_name.lower() == "firefox":
             driver = webdriver.Firefox()
        driver.maximize_window()
        return driver
        pass

    @staticmethod
    def close_browser(driver):
        if driver:
          driver.quit()
        pass

    @staticmethod
    def capture_screenshot(driver, name="screenshot"):
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/{name}.png")
        pass


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