import time
from datetime import datetime


class FiscalYearDataGenerator:
    """Generates dynamic, non-duplicating MM-YYYY start dates for Fiscal Year testing."""

    MIN_YEAR = 1900
    MAX_YEAR = 1923

    @staticmethod
    def generate_start_date(offset_years=0):
        """
        Generates a unique start date in 'MM-YYYY' format based on current Unix time.
        Constrained between 1900 and 2099 to match field validation limits.
        """
        base_year = 2026 + (int(time.time()) % 60) + offset_years
        unique_year = min(max(base_year, FiscalYearDataGenerator.MIN_YEAR), FiscalYearDataGenerator.MAX_YEAR - 1)
        return f"05-{unique_year}"

    @staticmethod
    def generate_update_date(current_start_date=None):
        """Generates a non-conflicting updated start date within the valid 1900-2099 range."""
        if current_start_date:
            month, year = current_start_date.split("-")
            new_year = int(year) + 2
            if new_year > FiscalYearDataGenerator.MAX_YEAR:
                new_year = int(year) - 5
            return f"{month}-{new_year}"
        return FiscalYearDataGenerator.generate_start_date(offset_years=5)

    @staticmethod
    def calculate_expected_end_date(start_date_str):
        """Calculates expected end date (MM-YYYY) based on start date."""
        month, start_year = start_date_str.split("-")
        m_int = int(month)
        s_year = int(start_year)

        end_month = f"{m_int - 1:02d}" if m_int > 1 else "12"
        end_year = s_year if m_int == 1 else s_year + 1
        return f"{end_month}-{end_year}"

    @staticmethod
    def calculate_expected_fiscal_year(start_date_str):
        """Calculates expected Fiscal Year range string (YYYY-YYYY) based on start date."""
        month, start_year = start_date_str.split("-")
        s_year = int(start_year)
        end_year = s_year if int(month) == 1 else s_year + 1
        return f"{s_year}-{end_year}"

    @staticmethod
    def calculate_expected_fy_code(start_date_str):
        """Calculates expected FY Code string (FYYYYY) based on start date."""
        _, start_year = start_date_str.split("-")
        return f"FY{start_year}"


class FillStartDate:
    def __init__(self, date_str=None):
        self._date_str = date_str or FiscalYearDataGenerator.generate_start_date()

    @property
    def date_str(self):
        return self._date_str

    @property
    def expected_end_date(self):
        return FiscalYearDataGenerator.calculate_expected_end_date(self._date_str)

    @property
    def expected_fiscal_year(self):
        return FiscalYearDataGenerator.calculate_expected_fiscal_year(self._date_str)

    @property
    def expected_fy_code(self):
        return FiscalYearDataGenerator.calculate_expected_fy_code(self._date_str)


class UpdateStartDate:
    def __init__(self, current_start_date=None):
        self._date_str = FiscalYearDataGenerator.generate_update_date(current_start_date)

    @property
    def date_string(self):
        return self._date_str

    @property
    def expected_end_date(self):
        return FiscalYearDataGenerator.calculate_expected_end_date(self._date_str)

    @property
    def expected_fiscal_year(self):
        return FiscalYearDataGenerator.calculate_expected_fiscal_year(self._date_str)

    @property
    def expected_fy_code(self):
        return FiscalYearDataGenerator.calculate_expected_fy_code(self._date_str)


class DropdownOptions:
            status_options = [
        "Active",
        "Inactive"
    ]