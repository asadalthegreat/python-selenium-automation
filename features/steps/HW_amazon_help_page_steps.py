from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

# Changing from script to step definition file

@given('I Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('I input Cancel Order into the search help library field')
def search_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')

@when ('I hit enter')
def search_help_hit_enter(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)

@then('Cancel Items or Orders text appears')
def verify_cancel_order_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    expected_result = 'Cancel Items or Orders'
    assert actual_result == expected_result, f'Error: Actual result {actual_result} does not match expected {expected_result}'

@then('Elements are visible on help page')
def verify_elements_are_visible_individually(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-section.a-spacing-extra-large.a-spacing-top-extra-large.ss-landing-container')
    context.driver.find_element(By.CSS_SELECTOR, '.a-section.a-spacing-large.ss-landing-container-wide')
    context.driver.find_element(By.ID, 'helpsearch')
    context.driver.find_element(By.CSS_SELECTOR, '.a-span12.a-column.a-spacing-top-small')
    context.driver.find_element(By.ID, 'csg-support-topics')
