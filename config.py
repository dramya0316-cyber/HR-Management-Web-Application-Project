from pathlib import Path

BASEURL = "https://opensource-demo.orangehrmlive.com"
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"
IMPLICITLY_WAIT = 10
EXPLICITLY_WAIT = 10
TESTDATA = "C:\\Users\\Sreelekha\\Desktop\\Guvi_projects\\HR Management Web Application Project\\test_data\\testdata.xlsx"


PROJECT_PATH = Path(__file__).parent

LOGS_DIR = PROJECT_PATH / "logs"
REPORTS_DIR = PROJECT_PATH / "reports"
SCREENSHOOT_DIR = PROJECT_PATH / "screenshots"

for directory in [LOGS_DIR, REPORTS_DIR, SCREENSHOOT_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
