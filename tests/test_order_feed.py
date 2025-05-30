import allure
from data import Ingredient
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:

    @allure.title('Получение деталей заказа из Лента заказов.')
    def test_click_on_order_from_feed(self):
        page = OrderFeedPage()
        page.click_on_order_from_feed()
        assert page.get_order_details()

    @allure.title('Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов».')
    def test_check_user_order_in_order_feed(self,order):
        page = OrderFeedPage()
        page.enter_to_personal_account(order[0], order[1])
        page.go_to_order_history()
        assert page.find_order_from_personal_account_in_order_feed()

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_all_completed_orders_counter(self, register):
        page = OrderFeedPage()
        count_before = int(page.get_completed_orders_counter())
        page.create_new_order(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_completed_orders_counter())
        assert count_after > count_before

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_today_completed_orders_counter(self, register):
        page = OrderFeedPage()
        count_before = int(page.get_completed_orders_counter_today())
        page.create_new_order_today(register[0], register[1], Ingredient.list_of_ingredients)
        count_after = int(page.get_completed_orders_counter_today())
        assert count_after > count_before

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_number(self, order):
        page = OrderFeedPage()
        order_number = str(order[3])
        assert page.wait_order_number_in_working_order_list(order_number)


