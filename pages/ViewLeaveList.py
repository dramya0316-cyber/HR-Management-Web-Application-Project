from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from pages.AssignLeavePage import AssignLeavePage
from pages.DashBoardPage import DashboardPage
from utilities.logger import LogGen
import time

logger = LogGen.loggen()


class ViewLeaveList(BasePage):
    LEAVE_LIST_TAB = (By.XPATH, "//a[text()='Leave List']")
    FROM_DATE_DROP_DOWN = (By.XPATH, "//div[@class='oxd-calendar-selector-month-selected']//i")
    FROM_DATE_LOC = (By.XPATH,
                     "(//label[text()='From Date']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//i)[1]")
    FROM_DATE_DROP_DOWN_SELECT = (By.XPATH, "//li[text()='September']")
    FROM_DATE_SELECT = (By.XPATH, "//div[text()='15']")
    SHOW_LEAVE_STATUS_DD = (By.XPATH,
                            "//label[normalize-space()='Show Leave with Status']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-select-text--after']//i")
    SHOW_LEAVE_STATUS_SELECT = (By.XPATH, "//span[text()='Scheduled']")
    SHOW_LEAVE_STATUS_XMARK = (By.XPATH, "//span[normalize-space()='Taken']//i")
    LEAVE_TYPE_DD = (By.XPATH,
                     "//label[normalize-space()='Leave Type']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-select-text--after']//i")
    LEAVE_TYPE_SELECT = (By.XPATH, "//span[normalize-space()='CAN - FMLA']")
    EMP_LOC = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMP_NAME_SELECT = (By.XPATH, "//div[@role='option']//span")
    EMP_NAME = "Thomas"
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    CONFIRMATION_LOCATION = (By.XPATH, "//div[@class='orangehrm-header-container']//span[contains(.,'Record Found')]")
    TO_DATE_LOC = (By.XPATH,
                   "//label[text()='To Date']/parent::div[@class='oxd-input-group__label-wrapper']/following-sibling::div/descendant::div[@class='oxd-date-input']/i")
    TO_DATE_MONTH_DD = (By.XPATH, "(//label[text()='To Date']/parent::div/following-sibling::div//i)[3]")
    TO_DATE_MONTH_SEP = (By.XPATH, "//li[@class='oxd-calendar-dropdown--option'][text()='September']")
    TO_DATE_SELECT_18 = (By.XPATH, "//div[@class='oxd-calendar-date'][text()='18']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_leave_list_tab(self):
        logger.info("*Clicking the Leave list tab ")
        self.find_element(self.LEAVE_LIST_TAB).click()
        self.wait.until(
            EC.visibility_of_element_located(self.FROM_DATE_LOC)
        )

    def from_date(self):
        logger.info("*Choose From date")

        self.find_element(self.FROM_DATE_LOC).click()
        self.find_element(self.FROM_DATE_DROP_DOWN).click()
        self.find_element(self.FROM_DATE_DROP_DOWN_SELECT).click()
        time.sleep(3)
        self.find_clickable_element(self.FROM_DATE_SELECT).click()

    def to_date(self):
        logger.info("*Choose To date")
        self.driver.execute_script("window.scrollTo(0, 0);")

        self.wait_for(EC.element_to_be_clickable(self.TO_DATE_LOC)).click()
        self.wait_for(EC.element_to_be_clickable(self.TO_DATE_MONTH_DD)).click()
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

    def show_leave_status(self):
        logger.info("*Displaying the Leave Status")
        element = self.wait_for(
            EC.visibility_of_element_located(self.SHOW_LEAVE_STATUS_DD)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.wait_for(
            EC.element_to_be_clickable(self.SHOW_LEAVE_STATUS_DD)
        ).click()

        self.wait_for(
            EC.element_to_be_clickable(self.SHOW_LEAVE_STATUS_SELECT)
        ).click()

    def leave_type(self):

        logger.info("*entering leave type")
        self.find_element(self.LEAVE_TYPE_DD).click()
        self.find_element(self.LEAVE_TYPE_SELECT).click()

    def employee_name(self):
        logger.info("*enter employee name")
        emp = self.find_element(self.EMP_LOC)
        emp.clear()
        emp.send_keys(self.EMP_NAME)

        employee = self.wait.until(
            EC.element_to_be_clickable(self.EMP_NAME_SELECT)
        )
        employee.click()

    def enter_search(self):
        logger.info("*Enter search button")
        self.find_element(self.SEARCH_BUTTON).click()

    def is_record_display(self):
        logger.info("*verifying Leave is Displayed")
        return self.find_element(self.CONFIRMATION_LOCATION).is_displayed()

    def view_leave_list(self):
        self.click_leave_list_tab()
        self.wait.until(
            EC.visibility_of_element_located(self.FROM_DATE_LOC)
        )
        self.from_date()
        self.to_date()
        self.show_leave_status()
        self.leave_type()
        self.employee_name()
        self.enter_search()
        header = self.driver.find_element(
            By.XPATH,
            "//div[@class='orangehrm-header-container']"
        )

        print(header.text)