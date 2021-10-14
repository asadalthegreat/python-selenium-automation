from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('I Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('I click Orders')
def input_to_search_field(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee maker')

@then('The sign in page is visible')
def verify_sign_in_page(context, header):
