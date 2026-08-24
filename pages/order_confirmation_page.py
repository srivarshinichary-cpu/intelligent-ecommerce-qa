from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderConfirmationPage:

    CONFIRMATION_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='complete-header']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CONFIRMATION_MESSAGE
            )
        ).text