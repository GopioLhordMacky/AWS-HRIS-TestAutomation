class CommonPaginationTests:
    """Reusable pagination test assertions across any page."""

    def assert_pagination_controls_visibility(self, page):
        # 1. Assert Rows Per Page Dropdown visibility
        assert page.is_row_per_page_dropdown_visible(), (
            f"[{page.__class__.__name__}] Rows per page dropdown is not visible."
        )

        # 2. Assert Pagination Information text visibility & non-emptiness
        pag_info = page.get_pagination_information()
        assert pag_info and len(pag_info) > 0, (
            f"[{page.__class__.__name__}] Pagination text missing or empty! Got: '{pag_info}'"
        )

        # 3. Assert Next Page Button visibility
        assert page.is_next_page_button_visible(), (
            f"[{page.__class__.__name__}] Next page button is not visible!"
        )

        # 4. Assert Previous Page Button visibility
        assert page.is_prev_page_button_visible(), (
            f"[{page.__class__.__name__}] Previous page button is not visible!"
        )