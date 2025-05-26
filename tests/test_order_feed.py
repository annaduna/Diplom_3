import allure
from api import ApiMethods
from data import Ingredient
from locators import OrderFeedPageLocators
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title('Получение деталей заказа из Лента заказов.')
    def test_click_on_order_from_feed(self, browser):
        page = OrderFeedPage(browser)
        assert page.get_order_details_by_clicking_on_order_in_feed(OrderFeedPageLocators.ORDER_IN_FEED)

    @allure.title('Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов».')
    def test_check_user_order_in_order_feed(self, browser, order):
        page = OrderFeedPage(browser)
        page.enter_to_personal_account(order[0], order[1])
        page.go_to_order_history()
        assert page.find_order_from_personal_account_in_order_feed()

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_all_completed_orders_counter(self, browser, register):
        page = OrderFeedPage(browser)
        count_before = int(page.get_element_text(OrderFeedPageLocators.ALL_ORDERS_COUNTER))
        ApiMethods.create_order(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_element_text(OrderFeedPageLocators.ALL_ORDERS_COUNTER))
        assert count_after > count_before

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_today_completed_orders_counter(self, browser, register):
        page = OrderFeedPage(browser)
        count_before = int(page.get_element_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))
        ApiMethods.create_order(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_element_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))
        assert count_after > count_before

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_number(self, browser, order):
        page = OrderFeedPage(browser)
        order_number = str(order[3])
        assert page.wait_order_number_in_working_order_list(order_number)

