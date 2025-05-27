import allure
from curl import urls
from locators import HomePageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestBasicFunctionality:

    @allure.title('Переход по клику на Конструктор.')
    def test_click_on_constructor_button(self, driver):
        page = LoginPage(driver)
        page.click_on_element(HomePageLocators.CONSTRUCTOR_BUTTON)
        assert urls.HOME_PAGE_URL == page.get_current_url()

    @allure.title('Переход по клику на Лента заказов.')
    def test_click_on_order_feed_button(self, driver):
        page = HomePage(driver)
        page.click_on_element(HomePageLocators.ORDER_FEED_BUTTON)
        assert urls.ORDER_FEED_URL == page.get_current_url()

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient(self, driver):
        page = HomePage(driver)
        page.click_on_element(HomePageLocators.BUN_INGREDIENT)
        assert "Детали ингредиента" == page.get_element_text(HomePageLocators.CARD_INGREDIENT_LABEL)

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_exit_from_ingredient_card(self, driver):
        page = HomePage(driver)
        page.click_on_element(HomePageLocators.BUN_INGREDIENT)
        page.wait_visibility_of_element(HomePageLocators.CARD_INGREDIENT_LABEL)
        page.scroll_and_click_on_element(HomePageLocators.EXIT_INGREDIENT_BUTTON)
        assert page.wait_visibility_of_element(HomePageLocators.MAIN_PAGE_TITLE)

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_check_counter_increase(self, driver):
        page = HomePage(driver)
        count_before = int(page.get_element_text(HomePageLocators.COUNT))
        page.drag_and_drop_element(driver, HomePageLocators.BUN_INGREDIENT, HomePageLocators.BASKET)
        count_after = int(page.get_element_text(HomePageLocators.COUNT))
        assert count_after > count_before

    @allure.title('Проверяем что залогиненный пользователь может оформить заказ')
    def test_check_order_creation(self, browser, register, driver):
        page = PersonalAccountPage(driver)
        page.open_url(urls.HOME_PAGE_URL)
        # page.do_login(register[0], register[1])
        page.do_login() # исправленный код
        page.drag_and_drop_element(driver, HomePageLocators.BUN_INGREDIENT, HomePageLocators.BASKET)
        page.click_on_element(HomePageLocators.PLACE_ORDER_BUTTON)
        assert page.wait_visibility_of_element(HomePageLocators.ACTIVE_ORDER_LABEL)