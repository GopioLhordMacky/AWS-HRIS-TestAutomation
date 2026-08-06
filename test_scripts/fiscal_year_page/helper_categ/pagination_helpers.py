import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Pagination, Table


def get_pagination_text(driver):
    """Returns the current page range text"""
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, Pagination.DISPLAYED_ROWS_TEXT)))
    return element.text.strip()


def go_to_next_page(driver):
    """Clicks the Next page button and waits for DOM update."""
    wait = WebDriverWait(driver, 10)
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Pagination.NEXT_PAGE_BUTTON)))
    next_btn.click()
    time.sleep(2)  # Allow React rendering to settle


def go_to_previous_page(driver):
    """Clicks the Previous page button and waits for DOM update."""
    wait = WebDriverWait(driver, 10)
    prev_btn = wait.until(EC.element_to_be_clickable((By.XPATH, Pagination.PREVIOUS_PAGE_BUTTON)))
    prev_btn.click()
    time.sleep(2)  # Allow React rendering to settle


def get_first_row_text(driver):
    """Returns the text of the first row to verify content updates across pages."""
    wait = WebDriverWait(driver, 10)
    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, Table.TABLE_ROWS)))
    return rows[0].text if rows else ""

def is_button_disabled(element):
    """
    Checks if a button element is disabled via HTML attribute or MUI class.
    """
    is_attr_disabled = element.get_attribute("disabled") is not None
    is_class_disabled = "Mui-disabled" in (element.get_attribute("class") or "")
    return is_attr_disabled or is_class_disabled

def change_rows_per_page(driver, option_value=10):
    """Clicks the 'Rows per page' dropdown and selects the specified option (e.g., 10, 20, 50, 100)."""
    wait = WebDriverWait(driver, 10)
    
    # 1. Click dropdown to open options menu
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, Pagination.ROWS_PER_PAGE_DROPDOWN)))
    dropdown.click()
    time.sleep(1)

    # 2. Select option matching option_value
    option_xpath = f"//li[@data-value='{option_value}'] | //li[contains(text(), '{option_value}')]"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    option.click()
    
    # Allow DOM re-render
    time.sleep(2)


def get_displayed_row_count(driver):
    """Returns the total number of table body rows currently rendered in the DOM."""
    rows = driver.find_elements(By.XPATH, Table.TABLE_ROWS)
    return len(rows)


def click_page_number(driver, page_num):
    """Clicks a specific page number button in the pagination bar."""
    wait = WebDriverWait(driver, 10)
    page_btn_xpath = f"//button[@aria-label='page {page_num}' or text()='{page_num}']"
    page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, page_btn_xpath)))
    page_btn.click()
    time.sleep(2)  # Allow DOM re-render


def is_page_selected(driver, page_num):
    """Checks if the given page number button has the active/selected visual class or attribute."""
    page_btn_xpath = f"//button[@aria-label='page {page_num}' or text()='{page_num}']"
    page_btn = driver.find_element(By.XPATH, page_btn_xpath)
    
    # Common MUI active indicators
    is_aria_current = page_btn.get_attribute("aria-current") == "true"
    is_selected_class = "Mui-selected" in (page_btn.get_attribute("class") or "")
    
    return is_aria_current or is_selected_class

def wait_for_valid_pagination(driver, timeout=10):
    """Waits until pagination text is loaded and not showing temporary '0–0 of 0' state."""
    wait = WebDriverWait(driver, timeout)
    wait.until(
        lambda d: get_pagination_text(d) != "0–0 of 0" and get_pagination_text(d) != ""
    )
