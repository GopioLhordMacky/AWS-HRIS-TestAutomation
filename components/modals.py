from imports.main_imports.main_imports import *
from locators.shared.shared_locators import ModalLocators
from pages.base_page import BasePage

class Modals(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_close(self):
        """Clicks the main Save button inside an active modal."""
        save_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.CLOSE_BUTTON))
        save_btn.click()

    def click_confirm(self):
        """Clicks the main Save button inside an active modal."""
        confirm_btn = self.wait.until(EC.element_to_be_clickable(ToastButtons.CONFIRM_BTN))
        confirm_btn.click()

    def click_cancel(self):
        """Clicks the main Save button inside an active modal."""
        save_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.CANCEL_BUTTON))
        save_btn.click()

    def click_save_only(self):
        """Clicks the main Save button inside an active modal."""
        save_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.SAVE_BUTTON))
        save_btn.click()

    def click_save_confirm(self):
        """Clicks Save/Confirm when a secondary confirmation button appears."""
        save_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.SAVE_BUTTON))
        save_btn.click()
        confirm_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.CONFIRM_BUTTON))
        confirm_btn.click()

    def click_save_cancel(self):
        """Clicks the Cancel button to dismiss modal changes."""
        cancel_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.CANCEL_BUTTON))
        cancel_btn.click()

    def click_close_x(self):
        """Clicks the 'X' button in the modal header to close it."""
        close_x_btn = self.wait.until(EC.element_to_be_clickable(ModalLocators.CLOSE_BUTTON_X))
        close_x_btn.click()

    def click_outside_modal(self):
        """Dismisses the modal by sending the ESC key to the active dialog or page."""
        modal = self.wait.until(EC.presence_of_element_located(ModalLocators.MODAL_CONTAINER))
        modal.send_keys(Keys.ESCAPE)

    def fill_edit_text_modal(self, field_identifier, new_text):
        """
        Clears existing text from a modal text input using CTRL/CMD+A + BACKSPACE 
        and types new text.
        """
        locator = ModalLocators.INPUT_BY_LABEL_OR_NAME(field_identifier)
        input_elem = self.wait.until(EC.element_to_be_clickable(locator))

        # Robust clear strategy for modern inputs (React/Angular)
        input_elem.send_keys(Keys.CONTROL + "a" if Keys.CONTROL else Keys.COMMAND + "a")
        input_elem.send_keys(Keys.BACKSPACE)
        input_elem.send_keys(new_text)

    def fill_edit_select_modal(self, field_identifier, new_option):
        """
        Clears and selects a new option in custom dropdowns (e.g., React-Select) or native selects inside modals.
        """
        locator = ModalLocators.SELECT_BY_LABEL_OR_NAME(field_identifier)
        select_elem = self.wait.until(EC.element_to_be_clickable(locator))

        # Clear existing selection in react-select style controls via keyboard shortcuts
        select_elem.send_keys(Keys.CONTROL + "a")
        select_elem.send_keys(Keys.BACKSPACE)
        select_elem.send_keys(new_option)
        select_elem.send_keys(Keys.ENTER)

    def verify_input_is_empty(self, locator) -> bool:
        """
        Checks if an input or textarea element's value is empty or contains only whitespace.

        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        # Retrieves value from 'value' attribute or visible text (for custom select/dropdown wrappers)
        value = element.get_attribute("value") or element.text or ""
        return value.strip() == ""

    # def clear_input_field(self, locator):
    #     element = self.driver.find_element(*locator)
    #     element.click()
    #     element.send_keys(Keys.CONTROL, "a")
    #     element.send_keys(Keys.BACKSPACE)

    def check_error_message(self, expected_text=None):
        """Checks if an inline or modal error message is visible and matches optional expected text."""
        try:
            error_elem = self.wait.until(EC.visibility_of_element_located(ModalLocators.ERROR_MESSAGE))
            actual_text = error_elem.text.strip()
            if expected_text:
                return expected_text.lower() in actual_text.lower()
            return len(actual_text) > 0
        except Exception:
            return False

    def check_toast_message(self, expected_text=None):
        """Checks if a popup toast message is visible and matches optional expected text."""
        try:
            toast_elem = self.wait.until(EC.visibility_of_element_located(ModalLocators.TOAST_MESSAGE))
            actual_text = toast_elem.text.strip()
            if expected_text:
                return expected_text.lower() in actual_text.lower()
            return len(actual_text) > 0
        except Exception:
            return False