from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BTN = (By.XPATH, "//button[@class='login-btn btn btn-outline-primary']")
    USER_AVATAR = (By.XPATH, "//div[contains(@class, 'avatar')] | //span[contains(text(), 'Welcome')]")
    SIDEBAR_MENU_ITEM = lambda page_name: (By.XPATH, f"//div[@class='sidePanelInnerContainer']//*[normalize-space(text())='{page_name}']")


class CommonTableLocators:
    TABLE_BODY = (By.XPATH, "//table/tbody")
    TABLE_HEADERS = (By.XPATH, "//thead/tr/th")
    HEADER_BY_NAME = lambda col_name: (By.XPATH, f"//thead/tr/th[contains(normalize-space(.), '{col_name}')]")
    TABLE_ROWS = (By.XPATH, "//tbody/tr")
    CELLS_BY_ROW = lambda row_idx: (By.XPATH, f"//tbody/tr[{row_idx}]/td")
    EDIT_BTN_BY_INDEX = lambda row_idx: (By.XPATH, f"//tbody/tr[{row_idx}]//*[contains(@data-testid, 'EditIcon') or contains(@class, 'container')]")
    EDIT_BTN_BY_VALUE = lambda cell_value: ( By.XPATH, f"//tbody/tr[td[normalize-space(.)='{cell_value}']]//*[contains(@data-testid, 'EditIcon') or contains(@class, 'container')]")
    EDIT_BTN_BY_COLUMN_VALUE = lambda col_idx, cell_value: (By.XPATH, f"//tbody/tr[td[{col_idx}][contains(normalize-space(.), '{cell_value}')]]//*[contains(@data-testid, 'EditIcon') or contains(@class, 'container')]")
    
class SearchLocators:
    GLOBAL_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search...']")

class DropdownLocators:
    DROPDOWN_CONTAINER_BY_LABEL = lambda label: (By.XPATH, f"//span[text()='{label}'] | //label[text()='Status']")
    # DROPDOWN_OPTION = lambda option_text: (By.XPATH, f"//select[@name ='{option_text}']")
    DROPDOWN_OPTION = lambda option_text: (By.XPATH, f"//option[normalize-space(text())='{option_text}'] | //li[normalize-space(text())='{option_text}']")

class PaginationLocators:
    ROWS_PER_PAGE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'MuiTablePagination-select') or contains(@class, 'MuiSelect-select')]")   
    ROWS_PER_PAGE_OPTION = lambda count: (By.XPATH, f"//li[contains(@class, 'MuiMenuItem-root') and (normalize-space(text())='{count}' or @data-value='{count}')]")    
    NEXT_PAGE_BTN = (By.XPATH, "//button[contains(translate(@aria-label, 'NEXT', 'next'), 'next page') or contains(@class, 'next') or .//*[contains(@data-testid, 'KeyboardArrowRight')]]")
    PREV_PAGE_BTN = (By.XPATH, "//button[contains(translate(@aria-label, 'PREVIOUS', 'previous'), 'previous page') or contains(@class, 'previous') or .//*[contains(@data-testid, 'KeyboardArrowLeft')]]")
    PAGINATION_INFO_TEXT = (By.XPATH, "//p[contains(@class, 'MuiTablePagination-displayedRows')]")

class ToggleSwitchLocators:
    TOGGLE_BY_ROW_AND_COL = lambda row_idx, col_idx: (By.XPATH, f"//tbody/tr[{row_idx}]/td[{col_idx}]//input[@type='checkbox']")

class TabNavigationLocators:
    SUB_TAB_BY_NAME = lambda tab_name: (By.XPATH, f"//div[contains(@role, 'tablist')]//button[normalize-space(text())='{tab_name}']")

class ViewModeLocators:
    TABLE_VIEW_BTN = (By.XPATH, "//button[@class='btn btn-primary' or @aria-label='Table View']")
    CARD_VIEW_BTN = (By.XPATH, "//button[@class='btn btn-outline-secondary' or @aria-label='Card View']")

class TreeTableLocators:
    EXPAND_CARET_BY_ROW = lambda row_idx: (By.XPATH, f"//tbody/tr[{row_idx}]//div[contains(@class, 'tree-expand-icon')] | "
    f"//tbody/tr[{row_idx}]//*[local-name()='svg' and (contains(@data-testid, 'ExpandMoreIcon') or contains(@data-testid, 'ChevronRightIcon'))]")    

class ModalLocators:
    # Modal Wrapper / Background
    MODAL_CONTAINER = (By.XPATH, "//div[@role='dialog'] | //div[contains(@class, 'modal-content')]")
    
    # Action Buttons
    SAVE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[normalize-space(text())='Save'] | //div[contains(@class, 'modal-content')]//button[normalize-space(text())='Save']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class = 'modal-close-button btn btn-danger']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-sm'] | //div[@role='dialog']//button[normalize-space(text())='Confirm']")
    CANCEL_BUTTON = (By.XPATH, "//button[@class='btn btn-light btn-sm'] | //div[@role='dialog']//button[normalize-space(text())='Cancel']")
    CLOSE_BUTTON_X = (By.XPATH, "//div[@role='dialog']//button[normalize-space(text())='Close'] | //button[@aria-label='Close']")

    # Messages & Alerts
    ERROR_MESSAGE = (By.XPATH, "//div[(@role='alert' or contains(@class, 'alert-warning')) and normalize-space(text()) != '']")    
    TOAST_MESSAGE = (By.XPATH, "//span [@class = 'toast-message']")
    INPUT_BY_LABEL_OR_NAME = lambda field_identifier: (
        By.XPATH, 
        f"//div[contains(@class, 'modal-content') or @role='dialog']//input[@name='{field_identifier}' or @id='{field_identifier}'] | "
        f"//div[contains(@class, 'modal-content') or @role='dialog']//label[normalize-space(text())='{field_identifier}']/following::input[1]"
    )
    
    SELECT_BY_LABEL_OR_NAME = lambda field_identifier: (
        By.XPATH, 
        f"//div[contains(@class, 'modal-content') or @role='dialog']//label[normalize-space(text())='{field_identifier}']/following::input[contains(@id, 'react-select') or contains(@class, 'select')][1] | "
        f"//div[contains(@class, 'modal-content') or @role='dialog']//select[@name='{field_identifier}']"
    )

class ToastButtons:
    CONFIRM_BTN = (By.XPATH, "//button[@class = 'btn btn-primary btn-sm']")
    CANCEL_BTN = (By.XPATH, "//button[@class = 'btn btn-light btn-sm']")