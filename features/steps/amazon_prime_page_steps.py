from selenium.webdriver.common.by import By
from behave import given, then


BENEFIT_MODULES = (By.ID, 'prime-benefit-module-more-content-item')


@given('I Open Amazon Prime page')
def open_amazon(context):
    context.app.amazon_prime_page.open_amazon_prime()

    # Without calling Page Object Method
    # context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_amount} benefit modules are present')
def verify_boxes_count(context, expected_amount):
    context.app.amazon_prime_page.verify_boxes_count(expected_amount)

# Without calling Page Object Method
# def verify_benefit_modules_count(context, expected_amount):
#     modules = context.driver.find_elements(*BENEFIT_MODULES)
#     assert len(modules) == int(expected_amount), f'Expected {expected_amount} modules, but got {len(modules)}'

