from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.SaveAdminPage import AdminPage
import time
from utilities.logger import LogGen

logger = LogGen.loggen()


class ViewAdminPage(BasePage):
    USER_NAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    USER_ROLE_DROP_DOWN = (By.XPATH,
                    "//label[text()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::i")
    USER_ROLE_DD_SELECT = (By.XPATH, "//div[@role='option']/span[text()='Admin']")
    EMPLOYEE_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SELECT = (By.XPATH, "//div[@role='listbox']/div[1]/span")
    EMP_NAME = "Thomas"
    STATUS_DROP_DOWN = (By.XPATH,
                 "//label[text()='Status']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::i")
    STATUS_DD_SELECT = (By.XPATH, "//span[text()='Enabled']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")

    def __init__(self, driver):
        super().__init__(driver)

    def Search_new_user(self, username):
        logger.info("*searching a user")
        self.find_element(self.USER_NAME).send_keys(username)
        self.find_clickable_element(self.USER_ROLE_DROP_DOWN).click()
        time.sleep(3)
        self.find_clickable_element(self.USER_ROLE_DD_SELECT).click()
        self.find_clickable_element(self.EMPLOYEE_NAME_TEXTBOX).send_keys(self.EMP_NAME)
        self.find_visible_element(self.EMPLOYEE_NAME_SELECT).click()
        self.find_clickable_element(self.STATUS_DROP_DOWN).click()
        self.find_element(self.STATUS_DD_SELECT).click()
        self.find_clickable_element(self.SEARCH_BUTTON).click()
        self.execute_script()

    def get_username_locator(self, username):
        logger.info("*Getting Username:{username} ")
        return (
            By.XPATH,
            f"//div[@role='table']//div[contains(normalize-space(), '{username}')]"
        )

    def is_username_displayed(self, username):
        logger.info("*verifying username as displayed")
        return self.find_element(self.get_username_locator(username)).is_displayed()