import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import config
from selene.api import browser
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages.base_page import BasePage
from data import *


chromedriver_path = ChromeDriverManager().install()


def setup():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.maximize_window()
    config.timeout = 10
    browser.set_driver(driver)


@pytest.fixture()
def open_base_url():
    setup()
    BasePage().open_url(base_url)
    yield
    pytest_exception_interact()
    browser.quit()


def pytest_exception_interact():
    allure.attach(
        name="Screenshot",
        body=browser.driver().get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG,
    )


@pytest.fixture(autouse=True)
def inject_config(request):
    pytest.config = request.config
