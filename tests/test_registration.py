import pytest
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from data import *
from helper import *


@allure.feature('Registration')
@pytest.mark.usefixtures('open_base_url')
class TestRegistration:
    @allure.title('User can register in approved state - Florida')
    def test_user_can_register_in_approved_state(self):
        phone = generate_phone()
        first_name = generate_first_name()
        email = generate_email()

        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name=Faker().last_name(),
                                      email=email,
                                      approved_state=True)
        DashboardPage().check_user_is_redirected_to_add_property_page()
        DashboardPage().check_user_property_title_is_correct(first_name=first_name)

    @allure.title('User can register in non-approved state - Alabama')
    def test_user_can_register_in_non_approved_state(self):
        phone = generate_phone()
        first_name = generate_first_name()
        email = generate_email()

        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name=Faker().last_name(),
                                      email=email,
                                      property_owner='Yes, I am already renting my property/s and looking for a property manager',
                                      non_approved_state=True)
        DashboardPage().check_user_is_redirected_to_overview_page()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)

    @allure.title('User can register in multiple approved states - Florida and Tennessee')
    def test_user_can_register_in_multiple_approved_state(self):
        phone = generate_phone()
        first_name = generate_first_name()
        email = generate_email()

        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name=Faker().last_name(),
                                      email=email,
                                      multiple_approved_states=True,
                                      property_owner='Not yet, looking to buy a property and rent it')
        DashboardPage().check_user_is_redirected_to_overview_page()
        DashboardPage().check_user_property_title_is_correct(first_name=first_name)

    @allure.title('User can register without indication of state')
    def test_user_can_register_without_indication_of_state(self):
        phone = generate_phone()
        first_name = generate_first_name()
        email = generate_email()

        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name=Faker().last_name(),
                                      email=email,
                                      property_owner='No, I am a renter')
        DashboardPage().check_user_is_redirected_to_overview_page()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)

    @allure.title('User cannot register with invalid number')
    def test_user_cannot_register_with_invalid_number(self):
        HomePage().submit_phone_number('00000')
        HomePage().check_error_text_for_mobile_is_correct('please provide a valid phone number')

    @allure.title('User cannot register without first name')
    def test_user_cannot_register_without_first_name(self):
        phone = generate_phone()
        email = generate_email()
        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name='',
                                      last_name=Faker().last_name(),
                                      email=email)
        HomePage().check_error_text_for_signup_form_is_correct('Required')

    @allure.title('User cannot register without last name')
    def test_user_cannot_register_without_last_name(self):
        first_name = generate_first_name()
        phone = generate_phone()
        email = generate_email()
        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name='',
                                      email=email)
        HomePage().check_error_text_for_signup_form_is_correct('Required')

    @allure.title('User cannot register without email')
    def test_user_cannot_register_without_email(self):
        first_name = generate_first_name()
        phone = generate_phone()
        HomePage().submit_phone_number(phone)
        HomePage().submit_signup_form(first_name=first_name,
                                      last_name=Faker().last_name(),
                                      email='test',
                                      property_owner='No, I am a renter')
        HomePage().check_error_text_for_signup_form_is_correct('Invalid email address')

    @allure.title('User can resend code')
    def test_user_can_resend_code(self):
        HomePage().submit_phone_number(registered_phone)
        sleep(60)
        HomePage().resend_otp_code()
