from selenium.webdriver.common.by import By
from behave import given, then


@given('I Open Amazon Prime page')
def open_amazon(context):
    context.app.amazon_prime_page.open_amazon_prime()


@then('Verify {expected_amount} benefit modules are present')
def verify_boxes_count(context, expected_amount):
    context.app.amazon_prime_page.verify_boxes_count(expected_amount)
