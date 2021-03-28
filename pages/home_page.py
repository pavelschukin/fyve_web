from selene.api import *
from pages.base_page import BasePage
import allure
from time import sleep

class HomePage(BasePage):

    # Locators

    continue_button = s('button[class*="login__submit-button"]')
    otp_input = s('#otp')
    resend_code_button = s('.property__verification__resend-button.btn.btn-link')
    phone_input = s('.login__input_number.form-control')

    # Methods

    @allure.step('Submit phone number')
    def submit_phone_number(self, phone):
        self.phone_input.set(phone)
        self.continue_button.click()
        self.spinner.should_not(be.visible)

    @allure.step('Submit signup form')
    def submit_signup_form(self, first_name, last_name, email, property_owner=None, approved_state=None,
                           multiple_approved_states=None, non_approved_state=None):
        first_name_input = s('#first_name')
        last_name_input = s('#last_name')
        email_input = s('#email')

        sleep(1)
        first_name_input.set(first_name)
        last_name_input.set(last_name)
        email_input.set(email)
        if property_owner:
            self.select_property_owner_type(property_owner)
        if approved_state:
            self.select_approved_state_or_states()
        if multiple_approved_states:
            self.select_approved_state_or_states(multiple_approved_states)
        if non_approved_state:
            self.select_non_approved_state()
        self.continue_button.click()
        self.spinner.should_not(be.visible)

    @allure.step('Select property owner type')
    def select_property_owner_type(self, type):
        customer_type = s('#customer_type')

        customer_type.click()
        browser.all('#customer_type > option').element_by(have.attribute('label', type)).click()

    @allure.step('Select approved state - Florida or states - Florida and Tennessee')
    def select_approved_state_or_states(self, multiple=None):
        states = ss('.login__states.row > button')

        if not multiple:
            states[0].click()
        else:
            states[0].click()
            states[1].click()

    @allure.step('Select non approved state - Alabama')
    def select_non_approved_state(self):
        other_states_button = s(by.xpath("//*[contains(text(),'Other states')]"))
        alabama = ss('label[for="stateAL"]')[1]
        select_button = s('div[class*=other_states] > .form-group > button')

        other_states_button.click()
        alabama.click()
        select_button.click()

    @allure.step('Submit otp code')
    def submit_otp_code(self, code):
        self.otp_input.set(code)
        self.continue_button.click()

    @allure.step('Resend otp code')
    def resend_otp_code(self):
        self.resend_code_button.click()
        self.otp_input.should(be.visible)

    @allure.step('Check error text for sign up form validation is correct')
    def check_error_text_for_signup_form_is_correct(self, text):
        error = s('.error')
        error.should(have.text(text))

    @allure.step('Check error text for mobile number validation is correct')
    def check_error_text_for_mobile_is_correct(self, text):
        error = s('.invalid-feedback')
        error.should(have.text(text))

    @allure.step('Click Continue')
    def click_continue(self):
        self.continue_button.click()
