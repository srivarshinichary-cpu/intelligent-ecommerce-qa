import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    options = webdriver.ChromeOptions()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    # Capture screenshot if the test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = (
            request.node.name + ".png"
        )

        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name
        )

        driver.save_screenshot(screenshot_path)

        print(
            f"\nScreenshot saved: {screenshot_path}"
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(
        item,
        "rep_" + rep.when,
        rep
    )