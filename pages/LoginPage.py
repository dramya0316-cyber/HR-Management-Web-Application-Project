import config
from utilities.logger import LogGen
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

logger = LogGen.loggen()


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_DROP_DOWN = (By.XPATH, "//img[@alt='profile picture']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")
    FORGOT_LINK = (By.XPATH, "//p[normalize-space()= 'Forgot your password?']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_username_field_present(self):
        return self.find_element(self.USERNAME)

    def is_username_field_enabled(self):
        return self.is_element_enabled(self.USERNAME)

    def is_password_field_present(self):
        return self.find_element(self.PASSWORD)

    def is_password_field_enabled(self):
        return self.is_element_enabled(self.PASSWORD)

    def enter_username(self, username):
        logger.info("*Entering the Username")
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        logger.info("*Entering the Password")
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        logger.info("*Click Login")
        self.click(self.LOGIN_BUTTON)

    def login_application(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        logger.info("*Logging out")
        dd = self.find_element(self.LOGOUT_DROP_DOWN)
        dd.click()

        logout = self.find_element(self.LOGOUT_BUTTON)
        logout.click()

    def forget_link(self):
        logger.info("*clicking forget link")
        self.find_clickable_element(self.FORGOT_LINK).click()








