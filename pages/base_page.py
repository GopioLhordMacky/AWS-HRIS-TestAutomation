from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.config import IMPLICIT_WAIT

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
        self.wait = WebDriverWait(driver, IMPLICIT_WAIT)

    def click(self, locator):
        """
        Wait until the element located by 'locator' is clickable, then click it.
        :param locator: tuple(By.METHOD, "locator_value")
        """
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            print(f"Error clicking element with locator {locator}: {e}")
            raise

    def type(self, locator, text):
        """
        Wait until the element located by 'locator' is visible,
        then clear any existing text and enter the new 'text'.
        :param locator: tuple(By.METHOD, "locator_value")
        :param text: string to type into the element
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error typing into element with locator {locator}: {e}")
            raise
