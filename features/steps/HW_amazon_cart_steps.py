from selenium.webdriver.common.by import By
from behave import when, then


@when('I click on the cart icon')
def cart_icon_click(context):
    context.app.cart_page.click_on_cart()
    # context.driver.find_element(By.ID, 'nav-cart').click()


@then('Cart is Empty text appears')
def verify_empty_cart_text(context):
    context.app.cart_page.verify_empty_cart()


@when('I select the helmet I want')
def click_helmet(context):
    context.app.cart_page.click_helmet()


@when('I click add to cart')
def add_to_cart(context):
    context.app.cart_page.click_add_to_cart()


@then('I verify the item is in the cart')
def verify_item_in_cart(context):
    context.app.cart_page.verify_cart_item()