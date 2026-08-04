import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def tab_navigation(driver, locator, keys=None, helper=None, *helper_args, **helper_kwargs):
    """
    Navigates to a target element using Tab keystrokes until focused, 
    then executes either a keystroke sequence or a custom helper function.

    :param driver: WebDriver instance
    :param locator: Tuple (By, "value") of the target element to reach via Tab
    :param keys: Optional key or string to send once focused (e.g., Keys.ENTER, "Text", Keys.SPACE)
    :param helper: Optional function/callable to execute after focusing the target element
    :param helper_args: Positional arguments to pass to the helper callable
    :param helper_kwargs: Keyword arguments to pass to the helper callable
    :return: bool (True if navigation and action succeeded, False otherwise)
    """
    try:
        target_element = driver.find_element(*locator)
        actions = ActionChains(driver)

        # 1. Tab until the active/focused element matches the target element
        max_tabs = 100
        tab_count = 0
        focused = False

        while tab_count < max_tabs:
            active_element = driver.switch_to.active_element
            if active_element == target_element:
                focused = True
                break

            # Send TAB to move focus to the next interactive element
            actions.send_keys(Keys.TAB).perform()
            tab_count += 1
            time.sleep(0.1)

        if not focused:
            print(f"[Tab Navigation Failed] Could not focus target locator {locator} within {max_tabs} tabs.")
            return False

        # 2. Execute custom helper callback if provided
        if helper and callable(helper):
            helper(driver, *helper_args, **helper_kwargs)

        # 3. Otherwise send specified keys/sequence if provided
        elif keys is not None:
            # Support passing a list/tuple of sequential keys e.g. [Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER]
            if isinstance(keys, (list, tuple)):
                for key in keys:
                    actions.send_keys(key).perform()
                    time.sleep(0.2)  # Brief delay between keystrokes for UI response
            else:
                key_to_send = getattr(Keys, keys) if isinstance(keys, str) and hasattr(Keys, keys) else keys
                target_element.send_keys(key_to_send)

        return True

    except Exception as e:
        print(f"[Tab Navigation Error] {e}")
        return False