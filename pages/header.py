from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)
