# imports/client_page_imports.py

# Framework & Timing
import pytest
import time

# Selenium Core & Components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

# Selenium Waits & Expected Conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2. Browser & Navigation Actions
from components.navigation import PageNavigation, KeyboardNavigation
from components.elements import ComponentVerifier, FormControls 
from components.modals import ModalActions, ModalNotifications
from components.tables import TableActions, TableData, TableSearch, TableSorting, TablePagination

# 3. Core Component Helpers
from data.client_page_inputs import *
from pages.client_page import *
from pages.base_page import *

# 4. All Categorized Locators
from locators.client_page_locators import (
    Login_Locators,
    Sidebar_Locators,
    Client_Locators,
    Filter_and_Search_Section,
    Update_Modal_Controls,
    Update_Modal_Inputs,
    Modal_Action_Buttons,
    Table_Headers_and_Rows,
    Row_Actions,
    Pagination_Section,
    Toast_Notifications_Validation_Messages,
    Toast_Buttons,
    Location_Management
)

