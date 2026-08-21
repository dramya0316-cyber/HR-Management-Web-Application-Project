from pages.LoginPage import LoginPage
import pytest
import config
from utilities.logger import LogGen
from utilities.ExcelUtilities import ExcelUtilites
from pages.ResetPasswordPage import ResetPasswordPage

logger = LogGen.loggen()


class TestLoginPage():
    logger.info("==========TEST CASE 01  Started==============")

    def test_validate_login_functionality(self, driver):
        logger.info("*Launch The Browser And URL")
        loginpage = LoginPage(driver)
        row = ExcelUtilites.get_row(config.TESTDATA, "data")

        for r in range(2, row + 1):
            logger.info("*Reading the data from Excel")
            username = ExcelUtilites.read_data(config.TESTDATA, "data", r, 1)
            password = ExcelUtilites.read_data(config.TESTDATA, "data", r, 2)

            logger.info("*Entering the Username and Password")
            loginpage.login_application(username, password)
            logger.info("*Checking The Validation")
            if "dashboard" in loginpage.get_url():
                logger.info("*Validation Success And Excel Updated as Passed")
                ExcelUtilites.write_data(config.TESTDATA, "data", r, 3, "passed")

            else:
                logger.info("*Validation Failed And Excel Updated as Failed")
                ExcelUtilites.write_data(config.TESTDATA, "data", r, 3, "failed")

    logger.info("==========TEST CASE 01 TEST PASSED=============")
    logger.info("========== TEST ENDED============")
