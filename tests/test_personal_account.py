import allure
from helpers.curl import urls
from pages.personal_account_page import PersonalAccountPage


class TestCheckPersonalAccount:

    @allure.title('Переход по клику на Личный кабинет c домашней страницы.')
    def test_click_personal_account_button(self, browser):
        page = PersonalAccountPage(browser)
        page.open_url(urls.HOME_PAGE_URL)
        page.click_on_personal_account_button()
        assert urls.LOGIN_PAGE_URL == page.get_current_url(), 'Страница Вход не загрузилась.'

    @allure.title('Переход в раздел История заказов.')
    def test_open_order_history(self, browser, register):
        page = PersonalAccountPage(browser)
        page.enter_to_personal_account(register[0], register[1])
        page.go_to_order_history()
        assert urls.ORDER_HISTORY_URL == page.get_current_url(), 'Страница История заказов не загрузилась.'

    @allure.title('Выход из Личного кабинета.')
    def test_logout_from_personal_account(self, browser, register):
        page = PersonalAccountPage(browser)
        page.enter_to_personal_account(register[0], register[1])
        page.do_logout()
        assert urls.LOGIN_PAGE_URL == page.get_current_url(), 'Страница Вход не загрузилась.'