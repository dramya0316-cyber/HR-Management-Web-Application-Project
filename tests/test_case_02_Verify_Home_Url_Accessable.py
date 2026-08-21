from pages.LoginPage import LoginPage
import pytest
import config
from utilities.logger import LogGen
from utilities.ExcelUtilities import ExcelUtilites
from pages.ResetPasswordPage import ResetPasswordPage

logger = LogGen.loggen()


class TestLoginPage():
    def test_verify_home_page_url(self, driver):

        logger.info("==========TEST CASE 02  STARTED==================")
        loginpage = LoginPage(driver)
        logger.info("*Opening the URL ")
        logger.info("*Validate the Home Page URL ")
        assert config.BASEURL in loginpage.get_url()
        logger.info("******** TEST CASE 02 PASSED ****************")
        logger.info("==========TEST ENDED==================")
