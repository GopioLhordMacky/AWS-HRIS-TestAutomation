class Login_Locators:
    USERNAME_FIELD = "//input[@name='email']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[contains(@class, 'login-btn')]"

class Sidebar_Locators:
    SIDEBAR_MENU = "//img[@src='/assets/calendar-104aac4d.svg']"
    FISCAL_YEAR_BUTTON = "//span[text()='Fiscal Year']"
    SIDEBAR_BODY = "//div[@class='sidePanelInnerContainer']"

class Options:
    STATUS_DROPDOWN = "//select[@name='status']"
    SEARCH_FIELD = "//input[@placeholder='Search...']"
    START_DATE = "//div[@class='react-datepicker__input-container']/input"
    END_DATE = "//input[contains(@class, 'automated-field')]"
    ROWS_PER_PAGE = "//input[contains(@class, 'MuiSelect-nativeInput')]"
    TOGGLE_BUTTON = "//input[@type='checkbox'] | //span[contains(@class, 'MuiSwitch-root')]"
    FY_CODE_INPUT = "//input[@name='fyCode']"
    FY_NAME_INPUT = "//input[@name='name']"

class Buttons:
    CLOSE_BUTTON = "//button[contains(@class, 'modal-close-button')]"
    SAVE_BUTTON = "//button[contains(@class, 'modal-button')]"
    ADD_FISCAL_YEAR_BUTTON = "//button[contains(@class, 'form-button')]"
    EDIT_BUTTON = "//div[@class = 'container']"
    X_BUTTON = "//button [@class = 'btn-close']"
    SORT_BUTTON = "//span[contains(@class, 'MuiTableSortLabel-root')]"

class Table:
    HEADER = "//thead[contains(@class, 'MuiTableHead-root')]"
    BODY = "//tbody[contains(@class, 'MuiTableBody-root')]"
    TABLE_ROWS = "//tbody[contains(@class, 'MuiTableBody-root')]/tr"

class Confirmation_Dialogue:
    CONFIRM_BUTTON = "//button[contains(text(), 'Confirm')]"
    CANCEL_BUTTON = "//button[contains(text(), 'Cancel')]"
    START_DATE_REQUIRED= "//div [@class = 'fade alert alert-warning alert-dismissible show']"
    TOAST_MESSAGE = "//span [@class = 'toast-message']"

class Modal:
    UPDATE_MODAL = "//div[@class = 'modal-content']"

class Pagination:
    ROWS_PER_PAGE_DROPDOWN = "//div[contains(@class, 'MuiTablePagination-select')]"
    ROWS_PER_PAGE_OPTION = "//li[@role='option' and @data-value='{count}']"
    DISPLAYED_ROWS_TEXT = "//p[contains(@class, 'MuiTablePagination-displayedRows')]"
    PREVIOUS_PAGE_BUTTON = "//button[@aria-label='Go to previous page']"
    NEXT_PAGE_BUTTON = "//button[@aria-label='Go to next page']"
