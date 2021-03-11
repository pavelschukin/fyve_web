import pytest
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from data import *
from helper import *


@allure.feature('Add Property')
@pytest.mark.usefixtures('open_base_url')
class TestAddProperty:
    @allure.title('User can register property in approved state - Florida as Individual '
                  'with mailing address in approved state')
    def test_user_can_register_property_in_approved_state_as_individual(self):
        phone = registered_phone
        otp = default_otp
        first_name = default_first_name
        street = Faker().street_address()

        HomePage().submit_phone_number(phone)
        HomePage().submit_otp_code(otp)
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)
        DashboardPage().click_add_property()
        DashboardPage().fill_property_address(zip='33482',
                                              street=street)
        DashboardPage().check_city_state_in_property_address_is_correct(city='Delray Beach',
                                                                        state='FL')
        DashboardPage().fill_owners_info(owners_name=first_name)
        DashboardPage().fill_mailing_address(zip='33482',
                                             street=street)
        DashboardPage().check_city_state_in_mailing_address_is_correct(city='Delray Beach',
                                                                       state='FL')
        DashboardPage().select_pricing_plan('Green')
        DashboardPage().mark_checkbox_add_property()
        DashboardPage().click_complete_button()
        DashboardPage().check_thank_you_text_is_displayed(first_name=first_name)
        DashboardPage().check_successfully_added_property_text_is_displayed()
        DashboardPage().check_property_card_text_is_displayed('Delray Beach, FL 33482, United States')
        HomePage().click_continue()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)

    @allure.title('User can register property in approved state - Tennessee as Entity '
                  'with mailing address in approved state')
    def test_user_can_register_property_in_approved_state_as_entity(self):
        phone = registered_phone
        otp = default_otp
        first_name = default_first_name
        street = Faker().street_address()

        HomePage().submit_phone_number(phone)
        HomePage().submit_otp_code(otp)
        DashboardPage().check_user_greeting_text_is_correct(first_name)
        DashboardPage().click_add_property()
        DashboardPage().fill_property_address(zip='37221',
                                              street=street)
        DashboardPage().check_city_state_in_property_address_is_correct(city='Nashville',
                                                                        state='TN')
        DashboardPage().fill_owners_info_entity(owners_name='Fyve LLC',
                                                authorized_person=first_name)
        DashboardPage().fill_mailing_address(zip='37221',
                                             street=street)
        DashboardPage().check_city_state_in_mailing_address_is_correct(city='Nashville',
                                                                       state='TN')
        DashboardPage().select_pricing_plan('Gold')
        DashboardPage().mark_checkbox_add_property()
        DashboardPage().click_complete_button()
        DashboardPage().check_thank_you_text_is_displayed(first_name)
        DashboardPage().check_successfully_added_property_text_is_displayed()
        DashboardPage().check_property_card_text_is_displayed('Nashville, TN 37221, United States')
        HomePage().click_continue()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)

    @allure.title('User can register property in approved state - Ohio as Individual '
                  'with mailing address in non-approved state')
    def test_user_can_register_property_in_approved_state_with_mailing_in_non_approved_state(self):
        phone = registered_phone
        otp = default_otp
        first_name = default_first_name
        street = Faker().street_address()

        HomePage().submit_phone_number(phone)
        HomePage().submit_otp_code(otp)
        DashboardPage().check_user_greeting_text_is_correct(first_name)
        DashboardPage().click_add_property()
        DashboardPage().fill_property_address(zip='44181',
                                              street=street)
        DashboardPage().check_city_state_in_property_address_is_correct(city='Cleveland',
                                                                        state='OH')
        DashboardPage().fill_owners_info(owners_name=first_name)
        DashboardPage().fill_mailing_address(zip='10001',
                                             street=street)
        DashboardPage().check_city_state_in_mailing_address_is_correct(city='New York',
                                                                       state='NY')
        DashboardPage().select_pricing_plan('Fyve')
        DashboardPage().mark_checkbox_add_property()
        DashboardPage().click_complete_button()
        DashboardPage().check_thank_you_text_is_displayed(first_name=first_name)
        DashboardPage().check_successfully_added_property_text_is_displayed()
        DashboardPage().check_property_card_text_is_displayed('Cleveland, OH 44181, United States')
        HomePage().click_continue()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)

    @allure.title('User can register property in non-approved state - New York as Individual')
    def test_user_can_register_property_in_non_approved_state(self):
        phone = registered_phone
        otp = default_otp
        first_name = default_first_name
        street = Faker().street_address()

        HomePage().submit_phone_number(phone)
        HomePage().submit_otp_code(otp)
        DashboardPage().check_user_greeting_text_is_correct(first_name)
        DashboardPage().click_add_property()
        DashboardPage().fill_property_address(zip='10001',
                                              street=street)
        DashboardPage().check_city_state_in_property_address_is_correct(city='New York',
                                                                        state='NY')
        DashboardPage().check_disclaimer_for_non_approved_states_is_visible()
        DashboardPage().click_complete_button()
        DashboardPage().check_thank_you_text_is_displayed(first_name=first_name)
        DashboardPage().check_successfully_added_property_text_is_displayed()
        DashboardPage().check_property_card_text_is_displayed('New York, NY 10001, United States')
        HomePage().click_continue()
        DashboardPage().check_user_greeting_text_is_correct(first_name=first_name)
