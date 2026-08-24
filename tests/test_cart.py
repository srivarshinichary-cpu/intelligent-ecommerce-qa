from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage



def test_add_product_to_cart(driver):

    # Login
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add product
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()    

    # Open cart
    products_page.open_cart()

    # Verify product
    cart_page = CartPage(driver)

    item = cart_page.get_cart_item()

    assert "Sauce Labs Backpack" in item