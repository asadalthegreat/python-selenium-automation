from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):

    SIGN_IN_MODULE = (By.CSS_SELECTOR, '.a-box-inner.a-padding-extra-large')

    def verify_sign_in_page_opens(self):
        self.wait_for_element_appear(*self.SIGN_IN_MODULE)

