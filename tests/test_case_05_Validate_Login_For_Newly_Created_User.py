from utilities.logger import LogGen
from pages.DashBoardPage import DashboardPage
import pytest
import config
from pages.LoginPage import LoginPage

logger = LogGen.loggen()


class TestDashboard:
    def test_create_newuser_and_validate_login(self, driver):
        logger.info("=====TEST CASE 05 started======")
        dashboard_page = DashboardPage(driver)
        dashboard_page.new_user_creation(driver)
        logger.info("validate the Dashboard URL")
        assert "dashboard" in dashboard_page.get_url()
        logger.info("==========TC 05 TEST PASSED===============")
        logger.info("==========TEST ENDED===============")