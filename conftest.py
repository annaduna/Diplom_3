import pytest
from api import ApiMethods
from data import Ingredient
from methods import register_new_user_and_return_login_password, register_new_user_and_order
from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()
        # else:
        #     raise ValueError(f"Unsupported browser: {browserName}")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.getWebdriver(browser_name)
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