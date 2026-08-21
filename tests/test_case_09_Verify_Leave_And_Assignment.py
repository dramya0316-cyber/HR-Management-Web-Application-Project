from pages.LoginPage import LoginPage
from pages.DashBoardPage import DashboardPage
from pages.AssignLeavePage import AssignLeavePage
import config
from pages.ViewLeaveList import ViewLeaveList
from utilities.logger import LogGen

logger = LogGen.loggen()


class TestLeave:

    def test_verify_leave(self, driver):
        logger.info("=====TESTCASE 09 started======")
        loginpage = LoginPage(driver)
        dashboard = DashboardPage(driver)
        assignleave = AssignLeavePage(driver)
        viewleave = ViewLeaveList(driver)
        loginpage.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        dashboard.click_leave_tab()
        assignleave.assign_leave()
        viewleave.view_leave_list()
        assert viewleave.is_record_display()
        logger.info("==========TEST CASE 09 TEST PASSED=========")
        logger.info("==========TEST ENDED===============")

