from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import BROWSER, HEADLESS, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT
import os

def get_driver():
    """
    Factory method returns WebDriver based on config.
    Supports: chrome, firefox, edge
    """
    browser = BROWSER.lower()
    
    if browser == "chrome":
        return _create_chrome_driver()
    elif browser == "firefox":
        return _create_firefox_driver()
    elif browser == "edge":
        return _create_edge_driver()
    else:
        raise ValueError(f"Unsupported browser: {browser}. Use: chrome, firefox, edge")

def _create_chrome_driver():
    """Chrome driver with optimal options."""
    options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False
    }

    options.add_experimental_option("prefs", prefs)
    
    # Basic options
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Headless mode
    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    
    # Performance
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-images")  # Faster loading
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    _apply_common_settings(driver)
    return driver

def _create_firefox_driver():
    """Firefox driver."""
    options = FirefoxOptions()
    if HEADLESS:
        options.add_argument("--headless")
    
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options
    )
    _apply_common_settings(driver)
    return driver

def _create_edge_driver():
    """Edge driver."""
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    if HEADLESS:
        options.add_argument("--headless")
    
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )
    _apply_common_settings(driver)
    return driver

def _apply_common_settings(driver):
    """Common settings for all drivers."""
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")