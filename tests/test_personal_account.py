import allure
from curl import urls
from pages.personal_account_page import PersonalAccountPage

class TestCheckPersonalAccount:

    @allure.title('Переход по клику на Личный кабинет c домашней страницы.')
    def test_click_personal_account_button(self, driver):
        page = PersonalAccountPage(driver)
        page.click_on_personal_account_button()
        assert urls.LOGIN_PAGE_URL == page.get_current_url()

    @allure.title('Переход в раздел История заказов.')
    def test_open_order_history(self, driver, register):
        page = PersonalAccountPage(driver)
        page.do_login()
        page.go_to_order_history()
        assert urls.ORDER_HISTORY_URL == page.get_current_url()

    @allure.title('Выход из Личного кабинета.')
    def test_logout_from_personal_account(self, driver, register):
        page = PersonalAccountPage(driver)
        page.enter_to_personal_account(register[0], register[1])
        page.do_logout()
        assert urls.LOGIN_PAGE_URL == page.get_current_url()