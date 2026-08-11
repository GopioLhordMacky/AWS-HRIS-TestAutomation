from imports.main_imports import *

class ClientFormData:
    VALID_INDUSTRY = "Automotive"
    VALID_COUNTRY = "Philippines"
    VALID_CONTACT_PERSON = "John Doe"
    VALID_EMAIL = "johndoe@example.com"
    VALID_PHONE = "091"
    VALID_ADDRESS = "123 Automation St., Metro Manila"
    INVALID_EMAIL = "invalid-email-format"
    LONG_CLIENT_NAME = "A" * 256 

    @classmethod
    def get_unique_client_name(cls, prefix="Automation Client"):
        # Use {prefix} here instead of {cls}
        return f"{prefix} {int(time.time())}"

class Options:
        industry_options = [
        "Automotive",
        "Healthcare / Medical Devices",
        "Information Technology Hardware",
        "Information Technology Services",
        "IT Services",
        "Life Sciences Technology"
    ]

        country_options = [
        "Philippines",
        "United States of America",
        "Singapore",
        "China" 
        ]

        status_options = [
        "Active",
        "Inactive"
    ]