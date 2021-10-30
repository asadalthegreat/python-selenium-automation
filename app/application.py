from pages.amazon_prime_page import AmazonPrimePage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignIn
from pages.cart_page import Cart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cart_page = Cart(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.amazon_prime_page = AmazonPrimePage(self.driver)
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
