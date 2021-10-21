from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, ".cs-help-container .help-service-content a[href='https://www.amazon.com/privacy']")
PRIVACY_NOTICE = (By.CSS_SELECTOR, 'div.help-content h1')


@given('I Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('I Click on Amazon Privacy Notice link')
def click_priv_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()

@then('I Verify Amazon Privacy Notice page is opened')
def verify_priv_notice_page(context):
    context.driver.wait.until(
        EC.visibility_of_element_located((PRIVACY_NOTICE)), message ='Error: Amazon Privacy Notice not visible')


@then('User can close new window and switch back to original')
def close_window_and_switch_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
