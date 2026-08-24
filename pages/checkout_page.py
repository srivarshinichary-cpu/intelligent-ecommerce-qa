from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.POSTAL_CODE
        ).send_keys(postal_code)

    def click_continue(self):

      self.wait.until(
        EC.element_to_be_clickable(self.CONTINUE_BUTTON)
      ).click()

      self.wait.until(
        EC.url_contains("checkout-step-two.html")
      )

    def click_finish(self):

        finish_button = self.wait.until(
            EC.visibility_of_element_located(self.FINISH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            finish_button
        )

        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_confirmation_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        ).text