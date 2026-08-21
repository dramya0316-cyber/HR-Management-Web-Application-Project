from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import config
from utilities.logger import LogGen

logger = LogGen.loggen()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICITLY_WAIT, poll_frequency=2)

    def wait_for(self, condition):
        return self.wait.until(condition)


    def find_element(self, locator):
        try:
            return self.wait_for(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            raise TimeoutException(
                f"Element not found: {locator}. Error: {str(e)}"
            )

    def find_visible_element(self, locator):
        try:
            element = self.wait_for(EC.visibility_of_element_located(locator))
            return element
        except:
            raise TimeoutException(f"Element not found: {locator}")

    def find_clickable_element(self, locator):
        try:
            element = self.wait_for(EC.element_to_be_clickable(locator))
            return element
        except:
            raise TimeoutException(f"Element not found: {locator}")

    def enter_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Error occurred while entering text in element {locator}: {str(e)}")

    def click(self, locator):
        try:
            element = self.find_clickable_element(locator)
            self.driver.execute_script("arguments[0].click();", element)


        except StaleElementReferenceException:
            logger.exception("----------Failed To Click Login Button--------")
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

        except TimeoutException:
            logger.exception("----------Failed To Click Login Button--------")
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

        except Exception as e:
            logger.exception("----------Failed To Click Login Button--------")
            raise Exception(f"Error occurred while clicking element {locator}: {str(e)}")

    def get_title(self):
        try:
            logger.info("Getting Title")
            return self.driver.title
        except Exception as e:
            logger.exception("----------Error occurred while getting page title---------")
            raise Exception(f"Error occurred while getting page title: {str(e)}")

    def get_url(self):
        try:
            logger.info("Getting Page URL")
            return self.driver.current_url
        except Exception as e:
            logger.exception("----------occurred while getting current URL----------")
            raise Exception(f"Error occurred while getting current URL: {str(e)}")

    def is_element_enabled(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except Exception as e:
            raise Exception(f"Error occurred while checking if element is enabled {locator}: {str(e)}")

    def find_elements(self, locator):
        try:
            self.wait_for(EC.presence_of_all_elements_located(locator))
            return self.driver.find_elements(*locator)
        except Exception as e:
            raise Exception(f"Error occurred while finding elements {locator}: {str(e)}")

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

    def execute_script(self):
        self.driver.execute_script("window.scrollTo(0, 0)")


