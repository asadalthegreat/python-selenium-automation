from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):

    EMPTY_CART = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty')
    HELMET = (By.XPATH, "//span[contains(text(),'ILM Bike Helmet')]")
    CARTITEM = (By.XPATH, "//span[contains(text(),'ILM Bike Helmet')]")
    ADDTOCART = (By.ID, 'add-to-cart-button')
    CARTICON = (By.ID, 'nav-cart')
     #CARTITEM = (By.CSS_SELECTOR, '.a-truncate-full.a-offscreen')


    def click_helmet(self):
        self.click(*self.HELMET)

    def click_add_to_cart(self):
        self.click(*self.ADDTOCART)

    def click_on_cart(self):
        self.click(*self.CARTICON)

    def verify_empty_cart(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART)

    def verify_cart_item(self):
        self.verify_text(
            'ILM Bike Helmet,Adjustable Lightweight Road Bicycle Helmet,Specialized Bike Helmet For Mens Womens Kids 5-14 Safety Protection(Ca…',
            *self.CARTITEM
        )
