import allure
from helpers.api import ApiMethods
from helpers.data import Ingredient
from helpers.locators import OrderFeedPageLocators
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title('Получение деталей заказа из Лента заказов.')
    def test_click_on_order_from_feed(self, browser):
        page = OrderFeedPage(browser)
        assert page.get_order_details_by_clicking_on_order_in_feed(OrderFeedPageLocators.order_in_feed)

    @allure.title('Проверка счётчика Выполнено за всё время.')
    def test_check_all_completed_orders_counter(self, browser, register):
        page = OrderFeedPage(browser)
        count_before = int(page.get_element_text(OrderFeedPageLocators.all_orders_counter))
        ApiMethods.create_order(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_element_text(OrderFeedPageLocators.all_orders_counter))
        assert count_after > count_before

    @allure.title('Проверка счётчика Выполнено за сегодня.')
    def test_check_today_completed_orders_counter(self, browser, register):
        page = OrderFeedPage(browser)
        count_before = int(page.get_element_text(OrderFeedPageLocators.today_orders_counter))
        ApiMethods.create_order(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_element_text(OrderFeedPageLocators.today_orders_counter))
        assert count_after > count_before

    @allure.title('Проверка номера оформленного заказа в разделе В работе.')
    def test_check_order_number(self, browser, order):
        page = OrderFeedPage(browser)
        order_number = '0'+str(order[3])
        assert page.wait_order_number_in_working_order_list(order_number)

    @allure.title('Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов».')
    def test_check_user_order_in_order_feed(self, browser, order):
        page = OrderFeedPage(browser)
        page.enter_to_personal_account(order[0], order[1])
        page.go_to_order_history()
        assert page.find_order_from_personal_account_in_order_feed()