from selenium.webdriver.common.by import By
from behave import given, then

# @Lana - benefit boxes don't appear when I see the amazon page,
# @Lana - but there are modules with testID prime-benefit-module-more-content-item

BENEFIT_MODULES = (By.ID, 'prime-benefit-module-more-content-item')


@given('I Open Amazon Prime page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_amount} benefit modules are present')
def verify_benefit_modules_count(context, expected_amount):
    modules = context.driver.find_elements(*BENEFIT_MODULES)
    assert len(modules) == int(expected_amount), f'Expected {expected_amount} modules, but got {len(modules)}'

