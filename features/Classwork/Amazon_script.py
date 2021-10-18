from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee maker')

driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

expected_result = '"coffee maker"'

# To compare that the actual and expected are identical. If not the same it will provide an error message.
# f stands for format - it's an f string in python - allows you to put variables in the string.
assert actual_result == expected_result, f'Error Actual {actual_result} does not match expected {expected_result}'

print("test passed")
driver.quit()
