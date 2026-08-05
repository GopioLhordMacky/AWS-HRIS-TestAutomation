import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://test.hris2.awsys-i.com")
LOGIN_URL = os.getenv("LOGIN_URL", "https://test.hris2.awsys-i.com/login")

VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

# Raise an error if credentials are not set via environment variables
if not VALID_USERNAME or not VALID_PASSWORD:
    raise ValueError("VALID_USERNAME and VALID_PASSWORD must be set as environment variables")

# Browser & Performance
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))

# Report settings
SCREENSHOT_ON_PASS = os.getenv("SCREENSHOT_ON_PASS", "false").lower() == "true"
