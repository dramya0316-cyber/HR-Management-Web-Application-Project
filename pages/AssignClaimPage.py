from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.ViewAdminPage import ViewAdminPage
from selenium.webdriver.support.ui import WebDriverWait
from utilities.logger import LogGen

logger = LogGen.loggen()


class AssignClaimPage(BasePage):
    ASSIGN_CLAIM = (By.XPATH, "//a[text()='Assign Claim']")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EVENT_DD = (By.XPATH,
                "//label[text()='Event']/ancestor::div[@class='oxd-input-group__label-wrapper']/following-sibling::div/descendant::i")
    EVENT_DD_VALUE = (By.XPATH, "//span[normalize-space()='Medical Reimbursement']")
    CURRENCY_DD = (By.XPATH,
                   "//label[text()='Currency']/ancestor::div[@class='oxd-input-group__label-wrapper']/following-sibling::div/descendant::i")
    CURRENCY_DD_VALUE = (By.XPATH, "//div[@role='option']//span[text()='United States Dollar']")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space()='Create']")
    REFERENCE_ID = (By.XPATH, "//label[normalize-space()='Reference Id']/parent::div/following-sibling::div//input")
    EMP_NAME = "Thomas"
    EMPLOYEE_NAME_SELECT = (By.XPATH, "//div[@role='listbox']/div[1]/span")


    def __init__(self, driver):
        super().__init__(driver)

    def click_assign_claim(self):
        logger.info("*click assign claim")
        self.find_element(self.ASSIGN_CLAIM).click()

    def enter_employee_name(self):
        logger.info("*Enter employee name")
        self.find_element(self.EMPLOYEE_NAME).send_keys(self.EMP_NAME)
        self.find_element(self.EMPLOYEE_NAME_SELECT).click()


    def enter_event(self):
        logger.info("*Enter event value")
        self.find_element(self.EVENT_DD).click()
        self.find_element(self.EVENT_DD_VALUE).click()

    def click_currency(self):
        logger.info("*Enter the currency")
        self.find_element(self.CURRENCY_DD).click()
        self.find_element(self.CURRENCY_DD_VALUE).click()

    def click_create(self):
        logger.info("*Click create")
        self.find_element(self.CREATE_BUTTON).click()

    def verify_reference_num_generate(self):
        logger.info("*verify the reference to be displayed")
        self.wait_for(EC.visibility_of_element_located(self.REFERENCE_ID)).is_displayed()
        logger.info("*Reference ID as displayed")

    def get_reference_id(self):
        logger.info("*getting the reference ID")
        WebDriverWait(self.driver, 15).until(
            lambda d: self.find_element(self.REFERENCE_ID).get_attribute("value") != ""
        )

        element = self.find_element(self.REFERENCE_ID)

        ref_id = element.get_attribute("value")

        print("Reference ID:", ref_id)

        return ref_id

    def assigning_claim(self):
        self.click_assign_claim()
        self.enter_employee_name()
        self.enter_event()
        self.click_currency()
        self.click_create()
        return self.get_reference_id()