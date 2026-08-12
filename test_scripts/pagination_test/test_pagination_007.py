import time
from pages.pagination_page import PaginationPage


def test_pagination_001(page: PaginationPage):
    """
        1. Capture initial page 1 pagination range text.
        2. Use tab_navigation to focus the Next button and press ENTER.
        3. Verify pagination range updates to page 2.
        4. Use tab_navigation to focus the Previous button and press SPACE.
        5. Verify pagination range returns back to page 1.    
    """
    time.sleep(2)

    # Step 1: Record initial pagination state
    initial_pag_info = page.get_pagination_information()

    # Step 2: Navigate via TAB to Next button and trigger with ENTER
    page.tab_navigation_next_btn()
    time.sleep(1.5)

    # Step 3: Verify page advanced
    next_pag_info = page.get_pagination_information()
    assert next_pag_info != initial_pag_info, (
        f"Keyboard activation via ENTER failed to advance page! "
        f"Initial: '{initial_pag_info}' | Current: '{next_pag_info}'"
    )

    # Step 4: Navigate via TAB to Previous button and trigger with SPACE
    page.tab_navigation_prev_btn()
    time.sleep(1.5)

    # Step 5: Verify page returned to initial range
    prev_pag_info = page.get_pagination_information()
    assert prev_pag_info == initial_pag_info, (
        f"Keyboard activation via SPACE failed to return to previous page! "
        f"Expected: '{initial_pag_info}' | Got: '{prev_pag_info}'"
    )