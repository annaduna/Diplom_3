import allure
from locators import HomePageLocators
from pages.base_page import BasePage
from curl import urls


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.open_url(urls.HOME_PAGE_URL)

    @allure.step('Кликаем на кнопку Конструктор.')
    def click_constructor_button(self):
        self.click_on_element(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на кнопку Лента заказов.')
    def click_order_feed_button(self):
        self.click_on_element(HomePageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликаем на ингредиент.')
    def click_on_ingredient(self):
        self.click_on_element(HomePageLocators.BUN_INGREDIENT)

    @allure.step('Получаем заголовок всплывающего окна ингредиента.')
    def get_ingredient_card_title(self):
        return self.get_element_text(HomePageLocators.CARD_INGREDIENT_LABEL)

    @allure.step('Кликаем на крестик в карточке ингредиента.')
    def close_ingredient_card(self):
        self.scroll_and_click_on_element(HomePageLocators.EXIT_INGREDIENT_BUTTON)

    @allure.step('Ждем заголовок')
    def wait_title(self):
        self.wait_visibility_of_element(HomePageLocators.MAIN_PAGE_TITLE)

    @allure.step('Получаем текст счетчика ингредиента')
    def get_counter_value(self):
        return self.get_element_text(HomePageLocators.COUNT)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop_ingredient_to_basket(self):
        self.drag_and_drop_element(HomePageLocators.BUN_INGREDIENT, HomePageLocators.BASKET)

    @allure.step('Получаем текст окна деталей ингредиента')
    def get_ingredient_details_text(self):
        return self.get_element_text(HomePageLocators.CARD_INGREDIENT_LABEL)