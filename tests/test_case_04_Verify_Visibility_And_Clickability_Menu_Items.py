from utilities.logger import LogGen
from pages.DashBoardPage import DashboardPage
import pytest
import config
from pages.LoginPage import LoginPage

logger = LogGen.loggen()


class TestDashboard:

    def test_verify_dashboard_menu(self, driver):
        logger.info("=====TEST CASE 04 started======")
        logger.info("******** Opening the URL *******************")
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        login_page.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        dashboard_page.click_menu_arrow()
        logger.info("Validate the presence of Dashboard Menu")
        assert dashboard_page.is_menubar_displayed()
        logger.info("Validate the enabled status of Dashboard Menu Items")
        assert dashboard_page.is_menubar_items_enabled()
        logger.info("==========TC 04 TEST PASSED===============")
        logger.info("==========TEST ENDED===============")



