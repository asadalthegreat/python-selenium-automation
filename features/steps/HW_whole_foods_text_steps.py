from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCTS = (By.CSS_SELECTOR, '.wfm-sales-item-card__regular-price')
PRODUCT_NAME =(By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')


@given('I Open Amazon Whole Foods page')
def open_product(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('I verify that every product has text Regular and product name')
def verify_regular_text(context):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        print(product_element.text)
        assert 'Regular' in product_element.text, f'Expected  Regular to be in element, but got {product_element}'

        product_name = product_element.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, 'Expected non-empty product name'