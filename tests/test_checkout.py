from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
from utils.test_data import load_test_data


def test_complete_checkout(driver):

    # Load test data
    test_data = load_test_data()

    login_data = test_data["valid_login"]
    customer = test_data["customer"]

    # Login
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    # Add product
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    # Open cart
    products_page.open_cart()

    # Checkout
    checkout_page = CheckoutPage(driver)

    checkout_page.click_checkout()

    checkout_page.enter_customer_details(
        customer["first_name"],
        customer["last_name"],
        customer["postal_code"]
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    # Verify order
    confirmation_page = OrderConfirmationPage(driver)

    message = confirmation_page.get_confirmation_message()

    assert "Thank you for your order!" in message