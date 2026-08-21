from pages.LoginPage import LoginPage
from pages.MyInfoPage import MyInfoPage
import config
from utilities.logger import LogGen

logger = LogGen.loggen()


class TestMyinfo:

    def test_verify_myinfo(self, driver):
        logger.info("==========TEST CASE 08  Started==========")
        loginpage = LoginPage(driver)
        myinfopage = MyInfoPage(driver)
        loginpage.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        myinfopage.click_myinfo()
        assert myinfopage.myinfo_tabs()
        logger.info("==========TEST CASE 08 PASSED===============")
        logger.info("==========TEST ENDED==================")



