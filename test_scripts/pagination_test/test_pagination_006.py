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