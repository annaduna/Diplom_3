from pages.base_page import BasePage
from helpers.curl import urls


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.HOME_PAGE_URL)