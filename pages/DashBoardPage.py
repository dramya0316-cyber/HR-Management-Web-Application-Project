import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
import config
from pages.SaveAdminPage import AdminPage
from utilities.logger import LogGen

logger = LogGen.loggen()


class DashboardPage(BasePage):
    MENUBAR_ARROW = (By.XPATH, "//button[@role='none']/i")
    MENUBAR_ITEMS = (By.XPATH, "//ul[@class='oxd-main-menu']//a")
    ADMIN_BUTTON = (By.XPATH, "//span[text()='Admin']")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    LEAVE_TAB = (By.XPATH, "//span[text()='Leave']")
    CLAIM_BUTTON = (By.XPATH, "//span[text()='Claim']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_menubar_displayed(self):
        logger.info("*verifying menubar as displayed")
        self.click(self.MENUBAR_ARROW)
        elements = self.find_elements(self.MENUBAR_ITEMS)
        logger.info("*menubar is displayed")
        return all(element.is_displayed() for element in elements)

    def is_menubar_items_enabled(self):
        logger.info("*verifying menubar is enable")
        self.click(self.MENUBAR_ARROW)
        menubar_items = self.find_elements(self.MENUBAR_ITEMS)
        logger.info("*menubar is enabled")
        return all(menu.is_enabled() for menu in menubar_items)

    def click_menu_arrow(self):
        logger.info("*Clicking Menu Arrow")
        self.click(self.MENUBAR_ARROW)

    def add_button_click(self):
        element = self.find_clickable_element(self.ADD_BUTTON)
        logger.info("*Clicking ADD BUTTON")
        element.click()

    def new_user_creation(self, driver):
        logger.info("*New User Creation Start*")
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver)
        logger.info("*Logging Using Admin Credentials*")
        login_page.login_application(config.VALID_USERNAME, config.VALID_PASSWORD)
        logger.info("*Navigate to Admin Page")
        self.find_element(self.ADMIN_BUTTON).click()
        logger.info("*Clicking ADD Button")
        self.add_button_click()
        logger.info("*Create The New Users")
        username, password = admin_page.user_creation()
        logger.info(f"*New User as Created Successfully: {username}")
        logger.info("*Logout With ADMIN credentials")
        login_page.logout()
        logger.info("*Login With New Credentials")
        login_page.login_application(username, password)
        self.wait.until(
            EC.url_contains("dashboard")
        )

    def click_admin(self):
        logger.info("*CLick admin Button")
        self.find_clickable_element(self.ADMIN_BUTTON).click()

    def user_creation(self, driver):
        admin = AdminPage(driver)

        username = admin.create_user()

        return username

    def click_add_button(self):
        self.find_element(self.ADD_BUTTON).click()

    def click_leave_tab(self):
        logger.info("*clicking Leave tab ")
        self.find_element(self.LEAVE_TAB).click()

    def click_claim(self):
        logger.info("*click Claim")
        self.wait_for(EC.visibility_of_element_located(self.CLAIM_BUTTON)).click()