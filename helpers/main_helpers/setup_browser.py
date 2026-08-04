import os
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

def close_browser(driver):
    if driver:
        driver.quit()

def capture_screenshot(driver, name="screenshot"):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{name}.png")

def wait_for_and_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def wait_and_type(driver, by, value, text, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    element.clear()
    element.send_keys(text)
    return element

def scroll_into_view(driver, locator_or_element):
    """
    Scrolls an element into view. 
    Accepts either a WebElement OR a locator tuple like (By.XPATH, "...").
    """
    if isinstance(locator_or_element, WebElement):
        element = locator_or_element
    else:
        element = driver.find_element(*locator_or_element)
        
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

def ensure_element_visible(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))