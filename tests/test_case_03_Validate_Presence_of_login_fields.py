from pages.LoginPage import LoginPage
import pytest
import config
from utilities.logger import LogGen
from utilities.ExcelUtilities import ExcelUtilites
from pages.ResetPasswordPage import ResetPasswordPage

logger = LogGen.loggen()


class TestLoginPage():
    def test_verify_presence_of_login_fields(self, driver):

        logger.info("==========TEST CASE 03  STARTED==================")

        loginpage = LoginPage(driver)
        logger.info("Validate the presence of Username and Password fields")
        assert loginpage.is_username_field_present()
        assert loginpage.is_password_field_present()
        logger.info("Validate the enabled status of Login Fields")
        assert loginpage.is_username_field_enabled()
        assert loginpage.is_password_field_enabled()
        logger.info("==========TEST CASE 03 PASSED==================")
        logger.info("==========TEST ENDED==================")