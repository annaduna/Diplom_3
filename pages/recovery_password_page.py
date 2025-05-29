import allure
from pages.base_page import BasePage
from locators import RecoveryPasswordPageLocators
from curl import urls

class RecoveryPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_url(urls.FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Вводим email и нажимаем на кнопку Восстановить.')
    def input_email_and_click_recovery_button(self):
        self.check_element_is_focused(RecoveryPasswordPageLocators.INPUT_EMAIL)
        self.send_keys_to_input(RecoveryPasswordPageLocators.INPUT_EMAIL,'test@test.ru')
        self.click_on_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON)
        self.wait_visibility_of_element(RecoveryPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Нажимаем на кнопку Показать/Скрыть пароль и проверяем что поле Пароль в фокусе.')
    def click_on_hide_show_password_button_and_check_field_focused(self):
        self.find_element_on_page(RecoveryPasswordPageLocators.PASSWORD_HIDE_SHOW_BUTTON)
        self.click_on_element(RecoveryPasswordPageLocators.PASSWORD_HIDE_SHOW_BUTTON)
        return self.check_element_is_focused(RecoveryPasswordPageLocators.PASSWORD_FIELD)