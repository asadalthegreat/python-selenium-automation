from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.amazon.com/rapids/register')

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

driver.find_element(By.ID, 'ap_customer_name')

driver.find_element(By.ID, 'ap_email')

driver.find_element(By.ID, 'ap_password')

driver.find_element(By.ID, 'ap_password_check')

driver.find_element(By.ID, 'continue')

driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age=0&openid']").click()


print("test passed")

driver.quit()