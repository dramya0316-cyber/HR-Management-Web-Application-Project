from pages.LoginPage import LoginPage
from pages.DashBoardPage import DashboardPage
from pages.EmployeeClaimPage import EmployeeClaimPage
from pages.AssignClaimPage import AssignClaimPage
import config
from utilities.logger import LogGen

logger = LogGen.loggen()


class TestClaim:

    def test_verify_claim(self, driver):
        logger.info("=====TEST CASE 10 started======")
        loginpage = LoginPage(driver)
        dashboard = DashboardPage(driver)
        employeeclaim = EmployeeClaimPage(driver)
        assignclaim = AssignClaimPage(driver)
        loginpage.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        dashboard.click_claim()
        ref_id = assignclaim.assigning_claim()
        employeeclaim.check_claim_list(ref_id)
        assert employeeclaim.is_ref_display(ref_id)
        logger.info("==========TC 10 TEST PASSED===============")
        logger.info("==========TEST ENDED===============")


