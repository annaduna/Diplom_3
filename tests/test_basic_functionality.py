import allure
from curl import urls
from locators import HomePageLocators
from pages.home_page import HomePage
from pages.personal_account_page import PersonalAccountPage


class TestBasicFunctionality:

    @allure.title('Переход по клику на Конструктор.')
    def test_click_on_constructor_button(self):
        page = HomePage()
        page.click_constructor_button()
        assert urls.HOME_PAGE_URL == page.get_current_url()

    @allure.title('Переход по клику на Лента заказов.')
    def test_click_on_order_feed_button(self):
        page = HomePage()
        page.click_order_feed_button()
        assert urls.ORDER_FEED_URL == page.get_current_url()

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient(self):
        page = HomePage()
        page.click_on_ingredient()
        assert "Детали ингредиента" == page.get_element_text(HomePageLocators.CARD_INGREDIENT_LABEL)

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_exit_from_ingredient_card(self):
        page = HomePage()
        page.click_on_ingredient()
        page.get_ingredient_card_title()
        page.close_ingredient_card()
        assert page.wait_title()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_check_counter_increase(self):
        page = HomePage()
        count_before = int(page.get_counter_value())
        page.drag_and_drop_ingredient_to_basket()
        count_after = int(page.get_counter_value())
        assert count_after > count_before

    @allure.title('Проверяем что залогиненный пользователь может оформить заказ')
    def test_check_order_creation(self, register):
        page = PersonalAccountPage()
        page.open_url()
        page.do_login()
        page.create_order()
        assert page.is_order_created()