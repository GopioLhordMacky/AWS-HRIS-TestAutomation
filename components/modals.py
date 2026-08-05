from imports.main_imports.main_imports import *
from locators.shared.shared_locators import ModalLocators

class ModalActions:
    @staticmethod
    def click_close(driver, timeout=10):
        """Clicks the main Save button inside an active modal."""
        wait = WebDriverWait(driver, timeout)
        save_btn = wait.until(EC.element_to_be_clickable(ModalLocators.CLOSE_BUTTON))
        save_btn.click()

    @staticmethod
    def click_confirm(driver, timeout=10):
        """Clicks the main Save button inside an active modal."""
        wait = WebDriverWait(driver, timeout)
        confirm_btn = wait.until(EC.element_to_be_clickable(ToastButtons.CONFIRM_BTN))
        confirm_btn.click()

    @staticmethod
    def click_cancel(driver, timeout=10):
        """Clicks the main Save button inside an active modal."""
        wait = WebDriverWait(driver, timeout)
        save_btn = wait.until(EC.element_to_be_clickable(ModalLocators.CANCEL_BUTTON))
        save_btn.click()

    @staticmethod
    def click_save_only(driver, timeout=10):
        """Clicks the main Save button inside an active modal."""
        wait = WebDriverWait(driver, timeout)
        save_btn = wait.until(EC.element_to_be_clickable(ModalLocators.SAVE_BUTTON))
        save_btn.click()

    @staticmethod
    def click_save_confirm(driver, timeout=10):
        """Clicks Save/Confirm when a secondary confirmation button appears."""
        wait = WebDriverWait(driver, timeout)
        save_btn = wait.until(EC.element_to_be_clickable(ModalLocators.SAVE_BUTTON))
        save_btn.click()
        confirm_btn = wait.until(EC.element_to_be_clickable(ModalLocators.CONFIRM_BUTTON))
        confirm_btn.click()

    @staticmethod
    def click_save_cancel(driver, timeout=10):
        """Clicks the Cancel button to dismiss modal changes."""
        wait = WebDriverWait(driver, timeout)
        cancel_btn = wait.until(EC.element_to_be_clickable(ModalLocators.CANCEL_BUTTON))
        cancel_btn.click()

    @staticmethod
    def click_close_x(driver, timeout=10):
        """Clicks the 'X' button in the modal header to close it."""
        wait = WebDriverWait(driver, timeout)
        close_x_btn = wait.until(EC.element_to_be_clickable(ModalLocators.CLOSE_BUTTON_X))
        close_x_btn.click()

    @staticmethod
    def click_outside_modal(driver, timeout=10):
        """Dismisses the modal by sending the ESC key to the active dialog or page."""
        wait = WebDriverWait(driver, timeout)
        modal = wait.until(EC.presence_of_element_located(ModalLocators.MODAL_CONTAINER))
        modal.send_keys(Keys.ESCAPE)

    @staticmethod
    def fill_edit_text_modal(driver, field_identifier, new_text, timeout=10):
        """
        Clears existing text from a modal text input using CTRL/CMD+A + BACKSPACE 
        and types new text.
        """
        wait = WebDriverWait(driver, timeout)
        locator = ModalLocators.INPUT_BY_LABEL_OR_NAME(field_identifier)
        input_elem = wait.until(EC.element_to_be_clickable(locator))
        
        # Robust clear strategy for modern inputs (React/Angular)
        input_elem.send_keys(Keys.CONTROL + "a" if Keys.CONTROL else Keys.COMMAND + "a")
        input_elem.send_keys(Keys.BACKSPACE)
        input_elem.send_keys(new_text)

    @staticmethod
    def fill_edit_select_modal(driver, field_identifier, new_option, timeout=10):
        """
        Clears and selects a new option in custom dropdowns (e.g., React-Select) or native selects inside modals.
        """
        wait = WebDriverWait(driver, timeout)
        locator = ModalLocators.SELECT_BY_LABEL_OR_NAME(field_identifier)
        select_elem = wait.until(EC.element_to_be_clickable(locator))
        
        # Clear existing selection in react-select style controls via keyboard shortcuts
        select_elem.send_keys(Keys.CONTROL + "a")
        select_elem.send_keys(Keys.BACKSPACE)
        select_elem.send_keys(new_option)
        select_elem.send_keys(Keys.ENTER)


class ModalNotifications:
    @staticmethod
    def check_error_message(driver, expected_text=None, timeout=5):
        try:
            wait = WebDriverWait(driver, timeout)
            error_elem = wait.until(EC.visibility_of_element_located(ModalLocators.ERROR_MESSAGE))
            actual_text = error_elem.text.strip()
            if expected_text:
                return expected_text.lower() in actual_text.lower() 
            return len(actual_text) > 0
        except Exception:
            return False

    @staticmethod
    def check_toast_message(driver, expected_text=None, timeout=5):
        try:
            wait = WebDriverWait(driver, timeout)
            error_elem = wait.until(EC.visibility_of_element_located(ModalLocators.TOAST_MESSAGE))
            actual_text = error_elem.text.strip()
            if expected_text:
                return expected_text.lower() in actual_text.lower() 
            return len(actual_text) > 0
        except Exception:
            return False