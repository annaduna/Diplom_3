import pytest
from api import ApiMethods
from curl import urls
from data import Ingredient
from methods import register_new_user_and_return_login_password, register_new_user_and_order
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(urls.HOME_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def register():
    register = register_new_user_and_return_login_password()
    yield register
    ApiMethods.delete_user(register[0], register[1], register[2])

@pytest.fixture
def order():
    order = register_new_user_and_order()
    ApiMethods.create_order(order[0], order[1], Ingredient.list_of_ingredients)
    yield order
    ApiMethods.create_user(order[0], order[1], order[2])