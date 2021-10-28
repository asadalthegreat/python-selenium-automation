from selenium.webdriver.common.by import By
from behave import given, when, then


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Dark Navy', 'Black', 'Dusty Rose']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error: expected {expected_colors[i]} did not match {current_color}'


# Another version
    # actual_colors = []
    #
    # for color in colors:
    #     color.click()
    #     actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
    #     print(f'{actual_colors}')
    #
    # assert expected_colors == actual_colors, f'Error: expected {expected_colors} did not match {actual_colors}'

@then('Verify user can click through degenerate colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Black', 'Navy', 'Asphalt', 'Royal Blue', 'Dark Heather', 'Heather Blue']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error: expected {expected_colors[i]} did not match {current_color}'

