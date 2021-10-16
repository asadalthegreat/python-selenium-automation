from selenium.webdriver.common.by import By
from behave import when, then


@when('I click on the cart icon')
def cart_icon_click(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Cart is Empty text appears')
def verify_empty_cart_text(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Error: Actual result {actual_result} does not match expected {expected_result}'


@when('I select the road bike I want')
def click_road_bike(context):
    context.driver.find_element(By.XPATH, "//span[text()='Tommaso Imola Endurance Aluminum Road Bike, Shimano Claris R2000, 24 Speeds, Black, White, Burnt Orange']").click()


@when('I click add to cart')
def cart_icon_click(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('I verify the item is in the cart')
def verify_item_in_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-truncate-cut').text
    print(actual_result)
    expected_result = "Tommaso Imola Endurance Aluminum Road Bike, Shimano Claris R2000, 24 Speeds - White - Extra Large"
    assert actual_result == expected_result, f'Error: Actual result {actual_result} does not match expected {expected_result}'
