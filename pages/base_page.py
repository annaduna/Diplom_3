import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Получаем URL активной страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Находим элемент на странице.')
    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('скрол до элемента страницы')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_visibility_of_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('клик по элементу страницы')
    def click_on_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('скролл и клик по элементу страницы')
    def scroll_and_click_on_element(self, locator):
        self.scroll_to_element(locator)
        self.wait_clickability_of_element(locator)
        self.click_on_element(locator)

    @allure.step('Вводим значение в поле')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Проверяем, что элемент активен для ввода.')
    def check_element_is_focused(self, locator):
        element = self.driver.find_element(*locator)
        is_focused = self.driver.execute_script("return document.activeElement === arguments[0];", element)
        return is_focused

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        self.wait_visibility_of_element(locator)
        return self.find_element_on_page(locator).text

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(5).perform()

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))