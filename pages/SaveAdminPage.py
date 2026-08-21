from selenium.webdriver.common.by import By
import time
import random
import string
from pages.BasePage import BasePage
from utilities.logger import LogGen

logger = LogGen.loggen()


class AdminPage(BasePage):
    USER_ROLE_DD = (By.XPATH,
                          "//label[normalize-space()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text--active')]")
    USER_ROLE_DD_ADMIN = (By.XPATH, "//div[@role='option']//span[text()='Admin']")
    STATUS_DD = (By.XPATH,
                       "//label[normalize-space()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text--active')]")
    STATUS_DD_ENABLED = (By.XPATH, "//div[@role='option']//span[text()='Enabled']")
    EMPLOYEE_LOC = (By.XPATH, "//input[@placeholder='Type for hints...']")
    USERNAME = (By.XPATH, "//label[normalize-space()='Username']/following::input[1]")
    PASSWORD = (By.XPATH, "//label[normalize-space()='Password']/following::input[1]")
    CON_PASSWORD = (By.XPATH, "//label[normalize-space()='Password']/following::input[2]")
    SAVE_BUTTON = (By.XPATH, "//button[text()=' Save ']")
    SUCCESS_SAVE_MESSAGE = (By.XPATH, "//div[@class='oxd-toast-start']/child::div[2]//p[2]")
    EMP_NAME = "Thomas"
    CHOOSE_EMP_NAME = (By.XPATH, "//div[@role='option']/span")

    def __init__(self, driver):
        super().__init__(driver)

    def create_user(self):
        logger.info("*Entering username:{username} and password:{password}")
        start_name = "test_user_"
        username = start_name + ''.join(random.choices(string.octdigits, k=8))
        password = "Usertest@1234"

        return username, password

    def user_creation(self):
        logger.info("*Users Creating")
        self.find_element(self.USER_ROLE_DD).click()
        self.find_visible_element(self.USER_ROLE_DD_ADMIN).click()

        self.find_element(self.STATUS_DD).click()
        self.find_visible_element(self.STATUS_DD_ENABLED).click()

        emp = self.find_element(self.EMPLOYEE_LOC)
        emp.send_keys(self.EMP_NAME)
        time.sleep(2)

        self.find_element(self.CHOOSE_EMP_NAME).click()
        username, password = self.create_user()

        user = self.find_element(self.USERNAME)
        user.send_keys(username)
        passw = self.find_element(self.PASSWORD)
        passw.send_keys(password)
        conf_p = self.find_element(self.CON_PASSWORD)
        conf_p.send_keys(password)

        self.find_element(self.SAVE_BUTTON).click()
        time.sleep(2)

        return username, password



