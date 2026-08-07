from selenium.webdriver.common.by import By


## LOCATORS ##

class Login_Locators:
    PAGE_HEADER = (By.XPATH, "//h2[text() = 'Client']" )
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='login-btn btn btn-outline-primary']")


class Sidebar_Locators:
    SIDEBAR_MENU = (By.XPATH, "//img[@src='/assets/calendar-104aac4d.svg']")
    CLIENT_BUTTON = (By.XPATH, "//span[text()='Client']")
    SIDEBAR_BODY = (By.XPATH, "//div[@class='sidePanelInnerContainer']")


class Client_Locators:
    TITLE = (By.XPATH, "//h2[text()='Client']")
    ADD_CLIENT_BUTTON = (By.XPATH, "//button[contains(., 'Add Client')]")


class Filter_and_Search_Section:
    INDUSTRY_FILTER_LABEL = (By.XPATH, "//span[text()='Industry'] | //label[text()='Industry']")
    INDUSTRY_FILTER_DROPDOWN = (By.XPATH, "//select[@name ='industry']")
    STATUS_FILTER_LABEL = (By.XPATH, "//span[text()='Status'] | //label[text()='Status']")
    STATUS_FILTER_DROPDOWN = (By.XPATH, "//select[@name ='status']")
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search...']")


class Update_Modal_Controls:
    MODAL_TITLE = (By.XPATH, "//div[text() = 'Update Client']")
    MODAL_CLOSE_X_BUTTON = (By.XPATH, "//button[contains(@class,'btn-close')]")


class Update_Modal_Inputs:
    MODAL_BODY = (By.XPATH, "//div[@class = 'modal-body']")
    CLIENT_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'modal-content')]//input[@name='name']")
    # INDUSTRY_SELECT = (By.XPATH, "//div[contains(@class, 'modal-content')]//div[contains(text(), 'Industry') and contains(@aria-describedby, 'placeholder')]")
    INDUSTRY_SELECT = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[text()='Industry']/following::input[contains(@id, 'react-select')][1]")
    COUNTRY_SELECT = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[text()='Country']/following::input[contains(@id, 'react-select')][1]")
    CONTACT_PERSON_INPUT = (By.XPATH, "//div[contains(@class, 'modal-content')]//input[@name='contactPerson']")
    EMAIL_ADDRESS_INPUT = (By.XPATH, "//div[contains(@class, 'modal-content')]//input[@name='emailAddress']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//div[contains(@class, 'modal-content')]//input[@name='phoneNumber']")
    ADDRESS_INPUT = (By.XPATH, "//div[contains(@class, 'modal-content')]//textarea[@name='address']")

    UPDATE_CLIENT_TITLE = (By.XPATH, "//div[contains(text(), 'Update Client')] | //div[contains(@class, 'modal-title h4')]//div[contains(text(), 'Update Client')]")

    # Change locator in Update_Modal_Inputs to target inside the modal container:
    INDUSTRY_UPDATE = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[text()='Industry']/following::input[1]")
    COUNTRY_UPDATE = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[text()='Country']/following::input[1]")

    # Add inside Update_Modal_Inputs if missing:
    LABEL_CLIENT_NAME = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Client Name')]")
    LABEL_INDUSTRY = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Industry')]")
    LABEL_COUNTRY = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Country')]")
    LABEL_CONTACT_PERSON = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Contact Person')]")
    LABEL_EMAIL = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Email')]")
    LABEL_PHONE = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Phone')]")
    LABEL_ADDRESS = (By.XPATH, "//div[contains(@class, 'modal-content')]//label[contains(text(), 'Address')]")


class Modal_Action_Buttons:
    CLOSE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[text()='Close']")
    SAVE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[text()='Save']")


class Table_Headers_and_Rows:
    NO_RESULTS_FOUND = (By.XPATH, "//h5[@class = 'mt-3']")
    TABLE_BODY = (By.XPATH, "//table/tbody")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    CLIENT_NAME_COLUMN = (By.XPATH, "//th[text()='Client Name']")
    INDUSTRY_COLUMN = (By.XPATH, "//th[text()='Industry']")
    COUNTRY_COLUMN = (By.XPATH, "//th[text()='Country']")
    CONTACT_PERSON_COLUMN = (By.XPATH, "//th[text()='Contact Person']")
    ACTIVE_COLUMN = (By.XPATH, "//th[text()='Active']")

    INDUSTRY_CELLS = (By.XPATH, "//table/tbody/tr/td[3]")
    COUNTRY_CELLS = (By.XPATH, "//table/tbody/tr/td[4]")
    CONTACT_PERSON_CELLS = (By.XPATH, "//table/tbody/tr/td[5]")
    ACTIVE_CELLS = (By.XPATH, "//table/tbody/tr/td[6]")


class Row_Actions:
    EDIT_BUTTON = (By.XPATH, "//div[@class = 'container']")
    ACTIVE_TOGGLE = (By.XPATH, "//table/tbody/tr//input[@type='checkbox' or contains(@class,'form-check-input')]")
class Pagination_Section:
    ROWS_PER_PAGE_LABEL = (By.XPATH, "//p[contains(text(),'Rows per page:')]")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Go to previous page']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Go to next page']")
    PAGINATION_INFO = (By.XPATH, "//p[contains(@class, 'MuiTablePagination-displayedRows')]")
    ROWS_PER_PAGE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'MuiTablePagination-select')]")
    PAGINATION_CONTAINER = (By.XPATH, "//div[contains(@class, 'MuiTablePagination-root') or contains(@class, 'pagination')]")



class Toast_Notifications_Validation_Messages:
    TOAST_MESSAGE = (By.XPATH, "//span [@class = 'toast-message']")
    FIELD_ERROR_MESSAGE = (By.XPATH, "//div[@role = 'alert' or contains(text(), 'Client Name is required!')]")
    DUPLICATE_ERROR = (By.XPATH, "//div[@role = 'alert' or contains(text(), 'A client with this name already exists')]")
    TOGGLE_CONFIRMATION = (By.XPATH, "//div[@class = 'text-white p-3 toast-body']")


class Toast_Buttons:
    CONFIRM_BTN = (By.XPATH, "//button[@class = 'btn btn-primary btn-sm']")
    CANCEL_BTN = (By.XPATH, "//button[@class = 'btn btn-light btn-sm']")


class Location_Management:
    LOCATION_SIDEBAR = (By.XPATH, "//span[text()='Location']")
    LOCATION_TABLE = (By.XPATH, "//table//tbody")
    COUNTRY_COLUMN_CELLS = (By.XPATH, "//table//tbody/tr/td[1]")