import pytest
from selenium import webdriver
from datetime import datetime
from pathlib import Path
import config


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="Chrome",
                     choices=["Chrome", "Edge", "firefox", "Safari"],
                     help="Support browser:Chrome,Edge,firefox,Safari")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "Safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"This Browser will not support: {browser}")

    driver.implicitly_wait(config.IMPLICITLY_WAIT)
    print("\n-------launching browser-------")
    driver.maximize_window()
    driver.get(config.BASEURL)
    yield driver
    print("\n-------Teardown browser-------")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            PROJECT_PATH = Path(__file__).parent
            SCREENSHOT_DIR = PROJECT_PATH / "screenshots"
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            driver.save_screenshot(str(SCREENSHOT_DIR / f"{item.name}-{timestamp}.png"))

