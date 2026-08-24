from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ITEM = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_item(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEM)
        ).text