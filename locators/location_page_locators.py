from selenium.webdriver.common.by import By


class Login_Locators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='login-btn btn btn-outline-primary']")


class Sidebar_Locators:
    SIDEBAR_MENU = (By.XPATH, "//img[@src = '/assets/location-78dc1609.svg']")
    LOCATION_BUTTON = (By.XPATH, "//span[text()='Location']")

class Modals:

    COUNTRY_MODAL = (By.XPATH, "//div[contains(@class, 'modal-content')][.//div[contains(@class, 'modal-title') and text()='Add Country']]")
    PROVINCE_MODAL = (By.XPATH, "//div[contains(@class, 'modal-content')][.//div[contains(@class, 'modal-title') and text()='Add Province']]")
    CITY_MODAL = (By.XPATH, "//div[contains(@class, 'modal-content')][.//div[contains(@class, 'modal-title') and text()='Add City']]")


class Options:
    LOCATION_OPTIONS = (By.XPATH, "//div[contains(@class, 'location-dropdown-menu')]")
    HEADER = (By.XPATH, "//thead[contains(@class, 'MuiTableHead-root')]")
    BODY = (By.XPATH, "//tbody[contains(@class, 'MuiTableBody-root')]")
    TABLE_ROWS = (By.XPATH, "//tbody[contains(@class, 'MuiTableBody-root')]/tr")

    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search...']")
    SEARCH_RESULT = (By.XPATH, "//table//tbody")
    TITLE = (By.XPATH, "//h2[text()='Locations']")

    TYPE_LABEL = (By.XPATH, "//span[text()='Type']")
    TYPE_DROPDOWN = (By.XPATH, "//select//option[@value='All']")
    STATUS_LABEL = (By.XPATH, "//span[text()='Status']")
    STATUS_DROPDOWN = (By.XPATH, "//select//option[@value='Active']")

    ADD_LOCATION_DROPDOWN_BUTTON = (By.XPATH, "//button[text()='Add Location']")

    ADD_COUNTRY_BUTTON = (By.XPATH, "//a[contains(., 'Add Country')]")
    ADD_PROVINCE_BUTTON = (By.XPATH, "//a[contains(., 'Add Province')]")
    ADD_CITY_BUTTON = (By.XPATH, "//a[contains(., 'Add City')]")

    SELECT_COUNTRY = (By.XPATH, "//div[contains(@class, 'control')][.//div[contains(text(), 'Select country')]]")
    SELECT_PROVINCE = (By.XPATH, "//div[contains(@class, 'control')][.//div[contains(text(), 'Select province')]]")
    SELECT_CITY = (By.XPATH, "//div[contains(@class, 'control')][.//div[contains(text(), 'Select city')]]")

    ISO_CODE = (By.XPATH, "//input[@id = 'react-select-4-input']")

    CLOSE_BUTTON = (By.XPATH, "//button[@class = 'modal-close-button btn btn-danger']")
    SAVE_BUTTON = (By.XPATH, "//button[@class = 'modal-button btn btn-primary']")

    LOCATION_NAME_COLUMN = (By.XPATH, "//span[text() = 'Location Name']")
    CODE_COLUMN = (By.XPATH, "//span[text() = 'Code']")
    ACTIVE_COLUMN = (By.XPATH, "//span[text() = 'Active']")

    ACTIVE_TOGGLE = (By.XPATH, "//table//tbody//tr//td[.//input[@type='checkbox' or contains(@class,'toggle')]]")
    ACTIVE_CONFIRM = (By.XPATH, "//button[text() = 'Confirm']")


class Validation_Message:
    VALIDATION_ALERT = (By.XPATH, "//div[@class='modal-body']")