from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    BACKPACK = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    CART = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK)
        ).click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()