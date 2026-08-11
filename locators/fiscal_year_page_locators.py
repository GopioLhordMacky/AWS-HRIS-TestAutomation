from selenium.webdriver.common.by import By
class Login_Locators:
    FISCAL_YEAR_TITLE = (By.XPATH, "//h2[text() = 'Fiscal Year']")
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'login-btn')]")

class Sidebar_Locators:
    SIDEBAR_MENU = (By.XPATH, "//img[@src='/assets/calendar-104aac4d.svg']")
    FISCAL_YEAR_BUTTON = (By.XPATH, "//span[text()='Fiscal Year']")
    SIDEBAR_BODY = (By.XPATH, "//div[@class='sidePanelInnerContainer']")

class Options:
    STATUS_DROPDOWN = (By.XPATH, "//select[@name='status']")
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Search...']")
    START_DATE = (By.XPATH, "//div[@class='react-datepicker__input-container']/input")
    END_DATE = (By.XPATH, "//input[contains(@class, 'automated-field')]")
    ROWS_PER_PAGE = (By.XPATH, "//input[contains(@class, 'MuiSelect-nativeInput')]")
    TOGGLE_BUTTON = (By.XPATH, "//input[@type='checkbox'] | //span[contains(@class, 'MuiSwitch-root')]")
    FY_CODE_INPUT = (By.XPATH, "//input[@name='fyCode']")
    FY_NAME_INPUT = (By.XPATH, "//input[@name='name']")

class Buttons:
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal-close-button')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal-button')]")
    ADD_FISCAL_YEAR_BUTTON = (By.XPATH, "//button[contains(@class, 'form-button')]")
    EDIT_BUTTON = (By.XPATH, "//div[@class = 'container']")
    X_BUTTON = (By.XPATH, "//button [@class = 'btn-close']")
    SORT_BUTTON = (By.XPATH, "//span[contains(@class, 'MuiTableSortLabel-root')]")

class Table:
    HEADER = (By.XPATH, "//thead[contains(@class, 'MuiTableHead-root')]")
    BODY = (By.XPATH, "//tbody[contains(@class, 'MuiTableBody-root')]")
    TABLE_ROWS = (By.XPATH, "//tbody[contains(@class, 'MuiTableBody-root')]/tr")

class Confirmation_Dialogue:
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    START_DATE_REQUIRED= (By.XPATH, "//div [@class = 'fade alert alert-warning alert-dismissible show']")
    TOAST_MESSAGE = (By.XPATH, "//span [@class = 'toast-message']")

class Modal:
    UPDATE_MODAL = (By.XPATH, "//div[@class = 'modal-content']")

class Pagination:
    ROWS_PER_PAGE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'MuiTablePagination-select')]")
    ROWS_PER_PAGE_OPTION = (By.XPATH, "//li[@role='option' and @data-value='{count}']")
    DISPLAYED_ROWS_TEXT = (By.XPATH, "//p[contains(@class, 'MuiTablePagination-displayedRows')]")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Go to previous page']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Go to next page']")