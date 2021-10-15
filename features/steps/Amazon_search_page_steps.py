from selenium.webdriver.common.by import By
from behave import given, when, then


@then('I verify {expected_result} text is shown')
def verify_amazon_found_results_text(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_result, f'Error Actual {actual_result} does not match expected {expected_result}'
