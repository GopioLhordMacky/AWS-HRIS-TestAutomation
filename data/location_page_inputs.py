# data/location_page_inputs.py

# 1. Existing/Seed Hierarchy Data (Guaranteed to pass independently)
VALID_COUNTRY_INPUT = {
    "country_name": "Japan",
    "expected_iso": "JP"
}

# Ensure this province belongs to a country that ALREADY exists in the seed database (e.g., 'Philippines' or 'China')
VALID_PROVINCE_INPUT = {
    "country_name": "Philippines",
    "province_name": "Laguna",
    "expected_code": "LAG"
}

# Ensure this city belongs to a province that ALREADY exists in the seed database (e.g., 'Anhui' under 'China')
VALID_CITY_INPUT = {
    "country_name": "China",
    "province_name": "Anhui",
    "city_name": "Bengbu"
}

# 2. Sequential End-to-End Test Chain Data
# For full workflow tests (Add Country -> Add Province to that Country -> Add City to that Province)
HIERARCHY_TEST_CHAIN = {
    "country": "South Korea",
    "province": "Gyeonggi-do",
    "city": "Suwon"
}