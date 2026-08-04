import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Setup: Initialize browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver  # Yields the driver instance to the test
    
    # Teardown: Automatically closes browser after test finishes
    driver.quit()