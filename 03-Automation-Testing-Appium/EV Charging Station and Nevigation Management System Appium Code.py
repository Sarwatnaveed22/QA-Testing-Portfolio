import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    options.app = r"C:\path\to\app-debug.apk"
    options.auto_grant_permissions = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_valid_ev_owner_login(driver):
    wait = WebDriverWait(driver, 20)

    # Example locators: update according to Appium Inspector
    email = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//*[contains(@text, 'Email')]")
    ))
    email.send_keys("testuser@gmail.com")

    password = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//*[contains(@text, 'Password')]")
    ))
    password.send_keys("123456")

    login_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//*[contains(@text, 'Login')]")
    ))
    login_btn.click()

    dashboard = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//*[contains(@text, 'Dashboard') or contains(@text, 'Nearby')]")
    ))

    driver.save_screenshot("screenshots/TC-05-valid-login.png")
    assert dashboard is not None
