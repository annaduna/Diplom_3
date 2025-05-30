from telnetlib import EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import PersonalAccountPageLocators, HomePageLocators
from curl import urls
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    def __init__(self):
        super().__init__()
        self.open_url(urls.HOME_PAGE_URL)

    @allure.step('Нажимаем на кнопку Личный кабинет и переходим на страницу авторизации.')
    def click_on_personal_account_button(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ENTRANCE_LABEL)

    @allure.step('Авторизуемся в личном кабинете с помощью логина и пароля.')
    def do_login(self, email, password):
        self.wait_clickability_of_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ENTRANCE_LABEL)
        self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_FIELD, data.DataForUser.user[email])
        self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_FIELD,data.DataForUser.user[password])
        self.click_on_element(PersonalAccountPageLocators.ENTRANCE_BUTTON)

    @allure.step('Нажимаем на кнопку Личный кабинет и переходим на страницу Профиль пользователя.')
    def go_to_user_profile_page(self):
        self.wait_clickability_of_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Входим в личный кабинет пользователя.')
    def enter_to_personal_account(self, email, password):
        self.open_url(urls.HOME_PAGE_URL)
        self.do_login(email, password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON))
        self.go_to_user_profile_page()

    @allure.step('Переходим в раздел История заказов.')
    def go_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON))
        self.check_element_is_focused(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выходим из личного кабинета.')
    def do_logout(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ENTRANCE_LABEL)

    @allure.step('Кликаем на кнопку Личный кабинет.')
    def go_to_personal_account(self):
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переходим в раздел История заказов.')
    def go_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выходим из личного кабинета.')
    def logout(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT_BUTTON)

    @allure.step('открыть юрл')
    def open_url(self):
        self.open_url(urls.HOME_PAGE_URL)

    @allure.step('Создаем заказ, добавляя ингредиент в корзину и оформляя заказ.')
    def create_order(self):
        self.drag_and_drop_element(HomePageLocators.BUN_INGREDIENT, HomePageLocators.BASKET)
        self.click_on_element(HomePageLocators.ACTIVE_ORDER_LABEL)

    @allure.step('Проверяем, что заказ был успешно создан.')
    def is_order_created(self):
        return self.wait_visibility_of_element(HomePageLocators.ACTIVE_ORDER_LABEL)