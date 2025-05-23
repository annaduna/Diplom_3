import allure
from locators import LoginPageLocators, RecoveryPasswordPageLocators
from curl import urls
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.LOGIN_PAGE_URL)

    @allure.step('Нажимаем на кнопку Восстановить пароль.')
    def click_on_recovery_password_button(self):
        self.scroll_and_click_on_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
        self.wait_visibility_of_element(RecoveryPasswordPageLocators.RECOVERY_PASSWORD_PAGE_TITLE)