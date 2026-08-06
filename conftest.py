import pytest
import allure
from allure_commons.types import AttachmentType
import os
import sys
from datetime import datetime
from utils.browser_factory import get_driver
from utils.auth_helpers import login_and_initial_setup
from pages.client_page import ClientPage
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

# from pages.department_page import DepartmentPage
# from pages.locators.department_locators import DepartmentLocators as Dept_Locator
import time

# Initialize the global list to prevent NameErrors
test_results = []
pytest_html = None

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

def pytest_sessionstart(session):
    """Run at session start."""
    pass

def pytest_sessionfinish(session, exitstatus):
    """Print report summary after all tests complete."""
    global test_results
    sys.stdout.write(f"\n------------------------------ Test Report Summary ------------------------------\n")
    for test_name, status in test_results:
        sys.stdout.write(f"{test_name}: {status}\n")
    sys.stdout.flush()

@pytest.fixture
def client_page(driver):
    # Pass authenticated driver into the child page class
    page = ClientPage(driver)
    page.driver.get(BASE_URL)
    login_and_initial_setup(driver, VALID_USERNAME, VALID_PASSWORD)
    return page

    
@pytest.fixture(scope="function")
def driver():
    """Starts the browser once for the whole test run."""
    _driver = get_driver()
    _driver.maximize_window()
    yield _driver
    _driver.quit()

@pytest.fixture(scope="session")
def driver_session():
    """Starts the browser once for the whole test run."""
    _driver = get_driver()
    _driver.maximize_window()
    yield _driver
    _driver.quit()

# --- LAYER 2: The Authentication ---
@pytest.fixture(scope="session")
def authenticated_driver(driver_session):
    """Logs in ONCE and ensures the Dashboard is ready."""
    driver = driver_session
    driver.get(BASE_URL)
    
    # Use the helper we discussed to Login + Wait for Dashboard
    login_and_initial_setup(driver, VALID_USERNAME, VALID_PASSWORD)
    
    return driver

@pytest.fixture
def client_page(authenticated_driver):
    """Passes the authenticated driver into ClientPage and navigates to the Client module."""
    page = ClientPage(authenticated_driver)
    page.driver.get("https://test.hris2.awsys-i.com/settings/client")
    return page

# --- Navigate to Department ---
# @pytest.fixture(scope="function")
# def department_page(authenticated_driver):
#     """Navigates to Department ONLY if needed."""
#     driver = authenticated_driver
#     page = DepartmentPage(driver)
    
#     if "department" not in driver.current_url.lower():
#         print("Navigating to Department module...")
#         navigate_to_module(driver, Dept_Locator.NAV_LINK, Dept_Locator.PAGE_TITLE)

#     return page

# @pytest.fixture(scope="function")
# def department_add_modal(department_page):
#     """Opens the modal and ensures it's cleaned up after the test."""
#     page = department_page
#     page.open_add_modal()
#     yield page

# @pytest.fixture(scope="function")
# def department_update_modal(department_page):
#     """Opens the modal and ensures it's cleaned up after the test."""
#     page = department_page
#     page.open_update_modal()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global test_results
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if report.passed:
            test_results.append((item.name, "Passed"))
        elif report.failed:
            test_results.append((item.name, "Failed"))
            
            # FIXED: Changed "driver" to "driver_session" to match your fixture name
            driver = item.funcargs.get("driver_session", None)
            
            if driver:
                # 1. Capture screenshot as raw bytes for Allure
                try:
                    screenshot_bytes = driver.get_screenshot_as_png()
                    allure.attach(
                        screenshot_bytes,
                        name=f"Failure_{item.name}",
                        attachment_type=AttachmentType.PNG
                    )
                except Exception as e:
                    print(f"\nFailed to attach screenshot to Allure: {e}")

                # 2. KEEPING YOUR OLD LOCAL/HTML BACKUP (Optional)
                screenshots_dir = "reports/screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name.replace(" ", "_")
                screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"
                
                # Save physical file locally
                driver.save_screenshot(screenshot_path)
                
                # Attach to old pytest-html report if plugin is active
                if pytest_html and hasattr(report, "extra"):
                    with open(screenshot_path, "rb") as img_file:
                        report.extra.append(pytest_html.extras.image(img_file.read()))

def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.passed:
            return "passed", "", "PASSED"
        if report.failed:
            return "failed", "F", "FAILED"