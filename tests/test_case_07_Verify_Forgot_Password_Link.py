from pages.LoginPage import LoginPage
import pytest
import config
from utilities.logger import LogGen
from utilities.ExcelUtilities import ExcelUtilites
from pages.ResetPasswordPage import ResetPasswordPage

logger = LogGen.loggen()


class TestLoginPage():
    def test_verify_forget_password_link(self, driver):

        logger.info("==========TEST CASE 07 STARTED==================")
        loginpage = LoginPage(driver)
        resetpassword = ResetPasswordPage(driver)
        loginpage.forget_link()
        resetpassword.forget_username()
        resetpassword.click_reset_button()
        assert "Reset" in resetpassword.reset_message()
        logger.info("==========TESTCASEC O7 TEST PASSED===============")
        logger.info("==========TEST ENDED==================")