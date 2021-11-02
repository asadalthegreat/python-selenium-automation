from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
    DEPT_LOCATOR = (By.CSS_SELECTOR, "option[value='search-alias={CATEGORY}']")


    def _get_expected_category(self, department):
        return [self.DEPT_LOCATOR[0], self.DEPT_LOCATOR[1].replace('{CATEGORY}', department)]

    def verify_correct_department(self, dept: str):
        locator = self._get_expected_category(dept)
        self.find_element(*locator)

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)
