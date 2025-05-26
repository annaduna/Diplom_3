import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

class BasePage:
    def __init__(self, driver):
        self.driver = driver

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

    @allure.step('Перетаскиваем элемент.')
    def drag_and_drop_element(self, dry, element_from, element_to):
        if browser == 'chrome':
            from_element = self.driver.find_element(*element_from)
            to_element = self.driver.find_element(*element_to)
            action = ActionChains(dry)
            action.drag_and_drop(from_element, to_element).perform()
            return action.drag_and_drop(from_element, to_element).perform()
        source_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_from))
        target_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_to))
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
        )

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))