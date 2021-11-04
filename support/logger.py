import logging

from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Handler creates a file test-automation.log if it's not there
handler = logging.FileHandler('./test_automation.log')
# Puts all the logs that you want to save
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MyListener(AbstractEventListener):
    logger = logger

    def before_find(self, by, value, driver):
        logger.info(f"Searching by {by} '{value}'...")

    def after_find(self, by, value, driver):
        logger.info(f"Found by {by} '{value}'")

    def on_exception(self, exception, driver):
        logger.error(exception)