from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import LogGen

logger = LogGen.loggen()


class EmployeeClaimPage(BasePage):
    EMPLOYEE_CLAIM_BUTTON = (By.XPATH, "//a[normalize-space()='Employee Claims']")
    STATUS_DROP_DOWN = (By.XPATH,
                 "//label[text()='Status']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::i")
    STATUS_DROP_DOWN_VALUE = (By.XPATH, "//span[text()='Initiated']")
    EVENT_NAME_DROP_DOWN = (By.XPATH,
                     "//label[text()='Event Name']/ancestor::div[@class='oxd-input-group__label-wrapper']/following-sibling::div/descendant::i")
    CLAIM_LIST_REF_ID = (By.XPATH, "//div[@class='oxd-table-body']/descendant::div[4]")
    EVENT_NAME = (By.XPATH, "//div[@role='listbox']//div//span[text()='Medical Reimbursement']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    REFERENCE_ID_LOCATION = (By.XPATH, "//label[normalize-space()='Reference Id']/parent::div/following-sibling::div//input")
    EMPLOYEE_NAME_INPUT_BOX = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SELECT = (By.XPATH, "//div[@role='listbox']/div[1]/span")
    EMP_NAME = "Thomas"

    def __init__(self, driver):
        super().__init__(driver)

    def click_employee_claims(self):
        logger.info("*clicking employee Claim")
        self.find_element(self.EMPLOYEE_CLAIM_BUTTON).click()

    def enter_employee_name(self):
        logger.info("*Entering Employee Name")
        self.find_clickable_element(self.EMPLOYEE_NAME_INPUT_BOX).send_keys(self.EMP_NAME)
        self.find_visible_element(self.EMPLOYEE_NAME_SELECT).click()

    def enter_reference_id(self, ref_id):
        logger.info("*Entering Reference ID")
        self.find_element(self.REFERENCE_ID_LOCATION).send_keys(ref_id)

    def enter_event_name(self):
        logger.info("*Enter Event type name")
        self.find_element(self.EVENT_NAME_DROP_DOWN).click()
        self.find_element(self.EVENT_NAME).click()

    def enter_status(self):
        logger.info("*Entering the status")
        self.find_element(self.STATUS_DROP_DOWN).click()
        self.find_element(self.STATUS_DROP_DOWN_VALUE).click()

    def enter_click_search(self):
        logger.info("*clicking search button")
        self.find_element(self.SEARCH_BUTTON).click()

    def verify_user_claim_list(self):
        logger.info("*verifying user claim in List")
        self.wait_for(
            EC.visibility_of_element_located(self.CLAIM_LIST_REF_ID)
        )

        logger.info("*User is displayed in Claim list")

    def is_ref_display(self, ref_id):
        actual_ref = self.wait_for(
            EC.visibility_of_element_located(self.CLAIM_LIST_REF_ID)
        ).text.strip()

        logger.info(f"Expected Ref ID: {ref_id}")
        logger.info(f"Actual Ref ID: {actual_ref}")

        return actual_ref == ref_id

    def check_claim_list(self, ref_id):
        self.click_employee_claims()
        self.enter_employee_name()
        self.enter_reference_id(ref_id)
        self.enter_event_name()
        self.enter_status()
        self.enter_click_search()
        self.verify_user_claim_list()

        return self.is_ref_display(ref_id)
