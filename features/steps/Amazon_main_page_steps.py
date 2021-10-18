from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a.nav_a')

@given('I Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {search_word} into amazon search')
def input_to_search_field(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('I click on amazon search icon')
def click_amazon_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then ('Verify hamburger menu icon is present')
def verify_ham_menu(context):
    print('\nFIND ELEMENT:\n')
    element = context.driver.find_elements(*HAM_MENU_ICON)
    print(element)
    print(type(element))

    print('\nFIND ELEMENTSSSS:\n')
    elements = context.driver.find_elements(*HAM_MENU_ICON)
    print(elements)
    print(type(elements))

    expected_count = 1
    actual_count = len(context.driver.find_elements(*HAM_MENU_ICON))
    assert expected_count == actual_count, f'Actual elements count {actual_count}, but expected {expected_count}'


@then('Verify {expected_amount} footer links are present')
def verify_footer_links(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(links)}'

