from selenium.webdriver.common.by import By

class LoginLocators:
    """Locators for Login page"""
    USERNAME_INPUT = (By.XPATH, "//input[@id='floatingInput']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='floatingPassword']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='login-errorPrompt']")