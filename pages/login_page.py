from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config.config import IMPLICIT_WAIT
from pages.base_page import BasePage
from locators.login_locators import LoginLocators as Locators

class LoginPage(BasePage):    
        
    def login(self, username, password):
        """
        Perform the login action by entering username and password, then clicking the login button.
        :param username: string username
        :param password: string password
        """
        self.type(Locators.USERNAME_INPUT, username)
        self.type(Locators.PASSWORD_INPUT, password)
        self.click(Locators.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Retrieve the error message text shown on invalid login.
        :return: string error message
        """
        return self.get_text(Locators.ERROR_MESSAGE)
