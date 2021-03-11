import uuid
import allure
import random
from time import sleep
from selene.api import *
from faker import Faker


@allure.step('Generate email')
def generate_email():
    return "{}".format(str(uuid.uuid4()))[:8] + '@example.com'


@allure.step('Generate first name')
def generate_first_name():
    return "Test " + Faker().first_name()


@allure.step('Generate phone')
def generate_phone():
    num = random.randrange(11111, 99999)
    return str(num) + '00000'


@allure.step('Scroll down')
def scroll_down_to_bottom():
    sleep(1)
    browser.driver().execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
