from pages.LoginPage import LoginPage
from pages.DashBoardPage import DashboardPage
from pages.ViewAdminPage import ViewAdminPage
from pages.SaveAdminPage import AdminPage
import config
import pytest
from utilities.logger import LogGen

logger = LogGen.loggen()


class TestViewAdmin:

    def test_validate_newly_created_user(self, driver):
        logger.info("==========TEST CASE 06  STARTED==========")
        loginpage = LoginPage(driver)
        dashboard = DashboardPage(driver)
        viewadmin = ViewAdminPage(driver)
        saveadminpage = AdminPage(driver)
        loginpage.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        dashboard.click_admin()
        dashboard.click_add_button()
        username, _ = saveadminpage.user_creation()
        dashboard.click_admin()
        viewadmin.Search_new_user(username)
        assert viewadmin.is_username_displayed(username)
        logger.info("==========TEST CASE 06 PASSED ===============")
        logger.info("==========TEST ENDED===============")







