from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a.nav_a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a[data-nav-role='signin']")

@given('I Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Input {search_word} into amazon search')
def input_to_search_field(context, search_word):
    context.app.header.input_search(search_word)


@when('I click on amazon search icon')
def click_amazon_search(context):
    context.app.header.click_search()


@when('Click Sign In from popup')
def click_sign_in_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message ='Error: Sign in button not clickable'
    ).click()


@when('Sign In popup appears')
def sign_in_appears(context):
    context.driver.wait.until(
        EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message ='Error: Sign in button not clickable')


@when('I wait for {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@then('I Verify Sign In popup disappears')
def click_sign_in_popup(context):
    context.driver.wait.until_not(EC.visibility_of_element_located((SIGN_IN_POPUP_BTN)),
                                  message ='Error: Sign in button is visible')
    assert context.driver.current_url == 'https://www.amazon.com/'

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

@when('I click on the Best Sellers link')
def click_on_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs']").click()

