from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import config
from utilities.logger import LogGen

logger = LogGen.loggen()


class ResetPasswordPage(BasePage):
    FORGOT_LINK_USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    RESET_PASSWORD = (By.XPATH, "//button[normalize-space()='Reset Password']")
    CONFIRM_MESSAGE = (By.TAG_NAME, "h6")

    def __init__(self, driver):
        super().__init__(driver)

    def forget_username(self):
        logger.info("Entering username")
        self.find_element(self.FORGOT_LINK_USERNAME).send_keys(config.VALID_USERNAME)

    def click_reset_button(self):
        logger.info("Clicking reset button")
        self.find_clickable_element(self.RESET_PASSWORD).click()

    def reset_message(self):
        logger.info("*Getting Confirmation Message")
        return self.find_visible_element(self.CONFIRM_MESSAGE).text