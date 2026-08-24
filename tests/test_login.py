from pages.login_page import LoginPage
from utils.test_data import load_test_data


def test_valid_login(driver):

    test_data = load_test_data()

    login_data = test_data["valid_login"]

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    test_data = load_test_data()

    login_data = test_data["invalid_login"]

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    error = login_page.get_error_message()

    assert "Username and password do not match" in error