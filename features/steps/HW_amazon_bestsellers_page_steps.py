from selenium.webdriver.common.by import By
from behave import given, then


NAVIGATION_LINKS = (By.CSS_SELECTOR, "a[href*='/ref=zg_bs_tab']")


# @Lana - There is some flakiness here - I get an amazon error page when I try to load the bestsellers page
# Opening that link works  when I run manually, but with selenium for some reason I get Amazon page "Sorry we couldn't find that page. Try the home page."
# However when I try the workaround opening the home page first (as below), then the second link works properly. Strange, but it works.
@given('I Open Amazon Bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs')


@then('Verify {expected_amount} navigation links are present')
def verify_navigation_link_count(context, expected_amount):
    nav_links = context.driver.find_elements(*NAVIGATION_LINKS)
    print(nav_links)
    assert len(nav_links) == int(expected_amount), f'Expected {expected_amount} modules, but got {len(nav_links)}'

