from selene.api import *
import allure


class BasePage:

    # Locators

    spinner = s('.spinner-border')

    # Methods
    @allure.step('Open url')
    def open_url(self, url):
        browser.open_url(url)
