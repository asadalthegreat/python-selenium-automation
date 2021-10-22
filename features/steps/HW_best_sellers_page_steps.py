from selenium.webdriver.common.by import By
from behave import given, when, then

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

######### OPTIONAL HW
@then('I click on each top link and verify a new page opens')
def click_top_links_and_verify_new_page(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'

