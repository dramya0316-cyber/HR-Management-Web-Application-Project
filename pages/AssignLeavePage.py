from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import LogGen
import time

logger = LogGen.loggen()


class AssignLeavePage(BasePage):
    ASSIGN_LEAVE = (By.XPATH, "//a[text()='Assign Leave']")
    EMP_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMP_NAME_SELECT = (By.XPATH, "//div[@role='option']//span")
    LEAVE_TYPE_DROP_DOWN = (By.XPATH, "//div[@class='oxd-select-text--after']//i")
    LEAVE_TYPE_SELECT = (By.XPATH, "//span[normalize-space()='CAN - FMLA']")
    FROM_DATE_LOC = (By.XPATH,
                     "//label[text()='From Date']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//i")
    FROM_DATE_DROP_DOWN = (By.XPATH, "//div[@class='oxd-calendar-selector-month-selected']/i")
    FROM_DATE_DROP_DOWN_SELECT = (By.XPATH, "//ul[@role='menu']//li[text()='September']")
    FROM_DATE_SELECT = (By.XPATH, "//div[text()='15']")
    TO_DATE_LOCATION = (By.XPATH,
                   "//label[text()='To Date']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//i")
    TO_DATE_MONTH_DROP_DOWN = (By.XPATH,
                        "//label[text()='To Date']/parent::div[@class='oxd-input-group__label-wrapper']/following-sibling::div/descendant::div[@class='oxd-calendar-selector-month-selected']//i")
    TO_DATE_MONTH_SEP = (By.XPATH, "//li[@class='oxd-calendar-dropdown--option'][text()='September']")
    TO_DATE_SELECT_18 = (By.XPATH, "//div[@class='oxd-calendar-date'][text()='18']")
    ASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='Assign']")
    EMP_NAME = "Thomas"
    CONFIRMATION_MESSAGE = (By.XPATH, "//p[contains(.,'Employee does not have sufficient leave balance')]")
    CONFIRMATION_OK_BUTTON = (By.XPATH, "//button[normalize-space()='Ok']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_assign_button(self):
        logger.info("*click assign button")
        self.find_clickable_element(self.ASSIGN_BUTTON).click()

    def click_assign_leave(self):
        logger.info("*click assign leave")
        self.find_clickable_element(self.ASSIGN_LEAVE).click()

    def enter_employee_name(self):
        logger.info("*enter employee name")
        self.find_element(self.EMP_NAME_INPUT).send_keys(self.EMP_NAME)
        self.find_element(self.EMP_NAME_SELECT).click()

    def enter_leave_type(self):
        logger.info("*entering leave type")
        self.find_element(self.LEAVE_TYPE_DROP_DOWN).click()
        self.find_element(self.LEAVE_TYPE_SELECT).click()

    def from_date(self):
        logger.info("*Choose From date")
        self.find_element(self.FROM_DATE_LOC).click()
        self.wait_for(EC.presence_of_element_located(self.FROM_DATE_DROP_DOWN)).click()
        self.find_element(self.FROM_DATE_DROP_DOWN_SELECT).click()
        self.find_element(self.FROM_DATE_SELECT).click()

    def to_date(self):
        logger.info("*Choose To date")

        self.wait_for(EC.element_to_be_clickable(self.TO_DATE_LOCATION)).click()

        self.wait_for(EC.element_to_be_clickable(self.TO_DATE_MONTH_DROP_DOWN)).click()

        months = self.driver.find_elements(By.XPATH, "//li[contains(@class,'oxd-calendar-dropdown--option')]")
        print("Months found:", len(months))

        for month in months:
            month.text
            if month.text == "September":
                month.click()
                break

        self.wait.until(
            EC.element_to_be_clickable(self.TO_DATE_SELECT_18)
        )

        self.driver.find_element(*self.TO_DATE_SELECT_18).click()

    def click_confirmation(self):
        logger.info("*click ok in confirmation")
        self.find_element(self.CONFIRMATION_OK_BUTTON).click()

    def confirmation_message_display(self):

        logger.info("Verifying confirmation message")

        element = self.find_visible_element(self.CONFIRMATION_MESSAGE)
        assert element.is_displayed()

    def assign_leave(self):
        self.click_assign_leave()
        self.enter_employee_name()
        self.enter_leave_type()
        self.from_date()
        self.to_date()
        self.click_assign_button()

        self.driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'Balance') or contains(text(),'Invalid')]"
        )

        self.confirmation_message_display()
        self.click_confirmation()