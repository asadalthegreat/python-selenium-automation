from selenium.webdriver.common.by import By
from behave import given, when, then


@given('I Open Amazon Whole Foods page')
def open_product(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('I verify {expected_number} items have \'Regular\' text')
def verify_regular_text(context, expected_number):
    reg_text = context.driver.find_elements(By.CSS_SELECTOR, '.wfm-sales-item-card__regular-price')
    actual_number = len(reg_text)
    assert expected_number == actual_number, f'error: expected {expected_number}, but got {actual_number}'


@then('I verify {expected_number} items have a product name')
def verify_product_has_name(context, expected_number):
    product_names = context.driver.find_elements(By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')
    actual_number = len(product_names)
    assert expected_number == actual_number, f'error: expected {expected_number}, but got {actual_number}'

