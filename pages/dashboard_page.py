from selene.api import *
from pages.base_page import BasePage
import allure
from time import sleep

class DashboardPage(BasePage):

    # Locators

    add_property_button = s('button[class*="property__submit"]')
    disclaimer = s('.property__disclaimer')
    complete_button = s('.property__submit.btn.btn-secondary')
    thank_you_title = s('.login__title')
    successful_added_property_text = s('.login__description.login__success_description')
    property_card_text = s('.login__property-text.card-text')
    owners_name_input = s('#ownersName')
    green_plan_button = s('button[class*="pricing_item__select_button"]')
    gold_plan_button = ss('button[class*="pricing_item__select_button"]')[1]
    fyve_plan_button = ss('button[class*="pricing_item__select_button"]')[2]

    # Methods

    @allure.step('Check user is redirected to Add Property page')
    def check_user_is_redirected_to_add_property_page(self):
        breadcrumb = ss('.breadcrumb-item')[1]
        breadcrumb.should(have.text('Add Property'))

    @allure.step('Check user is redirected to Overview page')
    def check_user_is_redirected_to_overview_page(self):
        breadcrumb = s('.breadcrumb-item')
        breadcrumb.should(have.text('Overview'))

    @allure.step('Check "Sorry we dont have service in your States" text is displayed')
    def check_sorry_service_message(self):
        s(by.text("Sorry, we don\'t have service yet in your States, but we are expanding fast so stay tuned!"))

    @allure.step('Check user greeting text is correct')
    def check_user_greeting_text_is_correct(self, first_name):
        greeting = s('.login__title')
        greeting.should(have.text(f"Good evening, {first_name}"))

    @allure.step('Check user property title text is correct')
    def check_user_property_title_is_correct(self, first_name):
        greeting = s('.property__title')
        greeting.should(have.text(f"Good evening, {first_name}"))

    @allure.step('Click Add property')
    def click_add_property(self):
        self.add_property_button.click()

    @allure.step('Fill property address')
    def fill_property_address(self, zip, street):
        zip_input = s('#ZIP')
        street_input = s('#street')

        zip_input.set(zip)
        street_input.set(street)

    @allure.step('Check city and state in Property Address are correct')
    def check_city_state_in_property_address_is_correct(self, city, state):
        city_input = s('#city')
        state_input = s('#state')
        city_input.should(have.attribute('value', city))
        state_input.should(have.attribute('value', state))

    @allure.step('Check city and state in Mailing Address are correct')
    def check_city_state_in_mailing_address_is_correct(self, city, state):
        city_input = ss('#city')[1]
        state_input = ss('#state')[1]
        city_input.should(have.attribute('value', city))
        state_input.should(have.attribute('value', state))

    @allure.step('Check disclaimer for non-approved states is visible')
    def check_disclaimer_for_non_approved_states_is_visible(self):
        self.disclaimer.should(have.text('By pressing the Complete button, '
                                    'you confirm that you have read in their entirely and agree to the following:'))

    @allure.step('Click Complete button')
    def click_complete_button(self):
        sleep(1)
        self.complete_button.should(be.enabled).click()

    @allure.step('Check successfully added property text is displayed')
    def check_successfully_added_property_text_is_displayed(self):
        self.successful_added_property_text.should(have.text("You have successfully added a property with Fyve"))

    @allure.step('Check thank you text is displayed')
    def check_thank_you_text_is_displayed(self, first_name):
        self.thank_you_title.should(have.text(f"Thank you, {first_name}."))

    @allure.step('Check property card text is displayed')
    def check_property_card_text_is_displayed(self, text):
        self.property_card_text.should(have.text(text))

    @allure.step('Check disclaimer for non-approved states is NOT visible')
    def check_disclaimer_for_non_approved_states_is_not_visible(self):
        self.disclaimer.should_not(be.visible)

    @allure.step('Fill Owners info')
    def fill_owners_info(self, owners_name):
        self.owners_name_input.set(owners_name)

    @allure.step('Fill Owners info - Entity')
    def fill_owners_info_entity(self, owners_name, authorized_person, title=None):
        owners_select = s('#owned')
        authorized_person_input = s('#authorizedPerson')
        title_input = s('#title')

        owners_select.click()
        browser.all('#owned > option').element_by(have.text('An entity')).click()
        self.owners_name_input.set(owners_name)
        authorized_person_input.set(authorized_person)
        if title:
            title_input.set(title)

    @allure.step('Fill Mailing Address')
    def fill_mailing_address(self, zip, street):
        zip_input = ss('#ZIP')[1]
        street_input = ss('#street')[1]

        zip_input.set(zip)
        street_input.set(street)

    @allure.step('Select pricing plan')
    def select_pricing_plan(self, plan):
        if plan == 'Green':
            self.green_plan_button.click()
        elif plan == 'Gold':
            self.gold_plan_button.click()
        elif plan == 'Fyve':
            self.fyve_plan_button.click()

    @allure.step('Mark checkbox Add property')
    def mark_checkbox_add_property(self):
        checkbox = s('.form-check-label')
        checkbox.should(be.enabled).click()
