from pages.base_page import Page
from selenium.webdriver.common.by import By

class AmazonPrimePage(Page):

    BOXES = By.CSS_SELECTOR, '.a-section.benefit-box'

    def open_amazon_prime(self):
        self.open_page('amazonprime')

    def verify_boxes_count(self, expected_amount):

        boxes = self.find_elements(*self.BOXES)
        assert len(boxes) == (expected_amount), f'Expected {expected_amount} but got {len(boxes)}'

