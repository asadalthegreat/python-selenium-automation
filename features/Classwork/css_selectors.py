from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

######## CSS  Locators Lesson ########

# By ID
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox').send_keys('coffee')

# By Class
driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')

# By Full attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

# By Partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

# Traveling through nodes
driver.find_element(By.CSS_SELECTOR, "a[href*='div#nav-xshop-container div#nav-xshop a']")

# Locators without using tag (tags are optional when searching by CSS selectors)
driver.find_element(By.CSS_SELECTOR, "[href*='div#nav-xshop-container div#nav-xshop a']")
driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold')

