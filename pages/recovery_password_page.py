import allure
from pages.base_page import BasePage
from helpers.locators import RecoveryPasswordPageLocators
from helpers.curl import urls


class RecoveryPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Вводим email и нажимаем на кнопку Восстановить.')
    def input_email_and_click_recovery_button(self):
        self.find_element_on_page(RecoveryPasswordPageLocators.input_email).send_keys('test@test.ru')
        self.click_on_element(RecoveryPasswordPageLocators.recovery_button)
        self.wait_visibility_of_element(RecoveryPasswordPageLocators.save_button)

    @allure.step('Нажимаем на кнопку Показать/Скрыть пароль и проверяем что поле Пароль в фокусе.')
    def click_on_hide_show_password_button_and_check_field_focused(self):
        self.find_element_on_page(RecoveryPasswordPageLocators.password_hide_show_button)
        self.click_on_element(RecoveryPasswordPageLocators.password_hide_show_button)
        return self.check_element_is_focused(RecoveryPasswordPageLocators.password_field)