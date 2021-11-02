from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    ESP_LANG_LINK = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    ENG_LANG_LINK = (By.XPATH, "//header[@id='navbar-main']//*[contains(text(), 'English - EN')]")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)

    def hover_over_language_options(self):
        lang = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()
        sleep(5)

    def select_department_by_alias(self, alias):
        select = Select(self.driver.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')

    def verify_lang_options_present(self):
        self.wait_for_element_appear(*self.ESP_LANG_LINK)
        self.find_element(*self.ENG_LANG_LINK)
