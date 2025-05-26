import allure
import time

import data
from locators import PersonalAccountPageLocators
from curl import urls
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.HOME_PAGE_URL)

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
        # self.find_element_on_page(PersonalAccountPageLocators.EMAIL_FIELD).send_keys(email)
        self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_FIELD, data.DataForUser.user[email]) # измененный код
        # self.find_element_on_page(PersonalAccountPageLocators.PASSWORD_FIELD).send_keys(password)
        self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_FIELD,data.DataForUser.user[password]) # измененный код
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
        time.sleep(1)
        self.go_to_user_profile_page()

    @allure.step('Переходим в раздел История заказов.')
    def go_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        time.sleep(1)
        self.check_element_is_focused(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выходим из личного кабинета.')
    def do_logout(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ENTRANCE_LABEL)