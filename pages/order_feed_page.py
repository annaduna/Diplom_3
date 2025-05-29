import allure
from api import ApiMethods
from locators import HomePageLocators, PersonalAccountPageLocators, OrderFeedPageLocators
from curl import urls
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.common.by import By

class OrderFeedPage(PersonalAccountPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.ORDER_FEED_URL)

    @allure.step('Нажимаем на заказ, получаем открытое окно с заказом.')
    def get_order_details_by_clicking_on_order_in_feed(self, locator):
        self.wait_visibility_of_element(locator)
        self.scroll_to_element(locator)
        self.click_on_element(locator)
        return self.wait_visibility_of_element(OrderFeedPageLocators.ORDER_CARD_LABEL)

    @allure.step('Находим на странице заказ и нажимаем на него.')
    def find_order_from_personal_account_in_order_feed(self):
        self.find_element_on_page(PersonalAccountPageLocators.ORDER_IN_ACCOUNT)
        order_id_in_account = self.get_element_text(PersonalAccountPageLocators.ORDER_IN_ACCOUNT)
        self.click_on_element(HomePageLocators.ORDER_FEED_BUTTON)
        locator = (By.XPATH, f".//p[text()='{order_id_in_account}']")
        self.wait_visibility_of_element(locator)
        order_in_feed = self.find_element_on_page(locator)
        return order_in_feed

    @allure.step('Ожидаем отображение номера заказа в разделе В работе')
    def wait_order_number_in_working_order_list(self, number):
        element = self.wait_visibility_of_element(OrderFeedPageLocators.ORDER_IN_WORK)
        return number in element.text

    @allure.step('Кликаем на заказ из ленты.')
    def click_on_order_from_feed(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_IN_FEED)

    @allure.step('Получаем детальную информацию о заказе.')
    def get_order_details(self):
        return self.wait_visibility_of_element(OrderFeedPageLocators.ORDER_CARD_LABEL)

    @allure.step('Ожидаем появление номера заказа в разделе В работе.')
    def wait_for_order_in_work(self, number):
        element = self.wait_visibility_of_element(OrderFeedPageLocators.ORDER_IN_WORK)
        return number in element.text

    @allure.step('Получаем текст счетчика выполненных заказов.')
    def get_completed_orders_counter(self):
        return self.get_element_text(OrderFeedPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('Создаем новый заказ через API.')
    def create_new_order(self, email, password, ingredients):
        ApiMethods.create_order(email, password, ingredients)

    @allure.step("получаем текст счетчика заказов за сегодня")
    def get_completed_orders_counter_today(self):
        return self.get_element_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Создаем новый сегодняшний заказ через API.')
    def create_new_order_today(self, email, password, ingredients):
        ApiMethods.create_order(email, password, ingredients)

