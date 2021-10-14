from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
# open webpage
driver.get('https://www.amazon.com/gp/help/customer/display.html')
# type into search field
driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')
# hit enter
driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)


# Verify the element matches the expected text
actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text

expected_result = 'Cancel Items or Orders'

### To compare that the actual and expected are identical. If not the same it will provide an error message.
### f stands for format - it's an f string in python - allows you to put variables in the string.
assert actual_result == expected_result, f'Error Actual {actual_result} does not match expected {expected_result}'

driver.quit()
