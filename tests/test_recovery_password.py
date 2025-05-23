import allure
from helpers.curl import urls
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage


class TestCheckRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль».')
    def test_open_recovery_password_page_by_button_click(self, browser):
        page = LoginPage(browser)
        page.click_on_recovery_password_button()
        assert urls.FORGOT_PASSWORD_PAGE_URL == page.get_current_url(), 'Страница Восстановление пароля не загрузилась.'

    @allure.title('Ввод почты и клик по кнопке «Восстановить» на странице «Восстановления пароля».')
    def test_input_email_input_and_click_recovery_password(self, browser):
        page = RecoveryPasswordPage(browser)
        page.input_email_and_click_recovery_button()
        assert urls.RESET_PASSWORD_PAGE_URL == page.get_current_url(), 'Страница Сброс пароля не загрузилась.'

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным.')
    def test_password_field_focused_if_press_show_password(self, browser):
        page = RecoveryPasswordPage(browser)
        page.input_email_and_click_recovery_button()
        assert page.click_on_hide_show_password_button_and_check_field_focused()