from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from utilities.logger import LogGen

logger = LogGen.loggen()


class MyInfoPage(BasePage):
    MYINFO_BUTTON = (By.XPATH, "//span[text()='My Info']")
    MYINFO_LIST = (By.XPATH, "//div[@role='tablist']//a")

    def __init__(self, driver):
        super().__init__(driver)

    def click_myinfo(self):
        logger.info("*clicking myinfo button")
        self.find_element(self.MYINFO_BUTTON).click()

    def myinfo_tabs(self):
        logger.info("*clicking myinfo tab")
        elements = self.find_elements(self.MYINFO_LIST)
        url = self.get_url().lower()

        for element in elements:
            option = element.is_displayed()
            if not option:
                return False
            if element.text.lower().replace(" ", "") in url:
                return True

        return False





