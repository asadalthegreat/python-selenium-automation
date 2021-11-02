from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Product(Page):

    SIGN_IN = (By.CSS_SELECTOR, '#nav-link-accountList')
    SIGNIN_COMPONENT = (By.CSS_SELECTOR, '#nav-al-container')

    def hover_mouse(self):
        sign_in = self.find_element(*self.SIGN_IN)
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_in)
        actions.perform()
        sleep(3)

    def verify_sign_in_component(self):
        self.wait_for_element_appear(*self.SIGNIN_COMPONENT)
