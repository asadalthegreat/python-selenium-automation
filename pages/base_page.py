class Page:
    def __int__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator): # (By.ID, 'value..')
        self.driver.find_element(*locator).click()

    def open_page(self, page_address=''):
        self.driver.get(f'{self.base_url}{page_address}')

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Actual text {actual_text} does not match expected text {expected_text}'
