from selenium.webdriver.common.by import By
from behave import given, when, then


@given('I Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {search_word} into amazon search')
def input_to_search_field(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('I click on amazon search icon')
def click_amazon_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
