# ==========================================
# SELENIUM & DRIVER MODULES
# ==========================================
import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait, Select
import platform
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

# ==========================================
# SHARED LOCATORS
# ==========================================
from locators.shared.shared_locators import (
    LoginLocators,
    CommonTableLocators,
    SearchLocators,
    DropdownLocators,
    PaginationLocators,
    ToggleSwitchLocators,
    TabNavigationLocators,
    ViewModeLocators,
    TreeTableLocators,
    ModalLocators,
    ToastButtons
)

# ==========================================
# MAIN COMPONENT IMPORTS
# ==========================================

from components.base_browser import (
    BrowserSetup,
    ElementActions,
)

from components.navigation import (
    Session,
    PageNavigation,
    KeyboardNavigation,
)

from components.elements import (
    ComponentVerifier,
    FormControls,
)

from components.modals import (
    ModalActions,
    ModalNotifications,
)

from components.tables import (
    TableData,
    TableActions,
    TableSearch,
    TableSorting,
    TablePagination,
)