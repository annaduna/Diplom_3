import allure
import requests
import random
import string
from helpers.api import ApiMethods
from helpers.data import Ingredient
from helpers.curl import urls

@allure.step('Регистрируем нового пользователя.')
def register_new_user_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    email = generate_random_string(10)+'@mail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(urls.USER_REGISTER_HANDLE, data=payload)

    if response.status_code == 200:
        login_pass = [email, password, name]

    return login_pass

@allure.step('Генерируем строку, состоящую только из букв нижнего регистра.')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

data = generate_random_string(9)
data_email = generate_random_string(9)+'@email.ru'
registration = register_new_user_and_return_login_password

@allure.step('Регистрируем уникального пользователя.')
def register_new_user_and_order():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    email = generate_random_string(10)+'@mail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(urls.USER_REGISTER_HANDLE, data=payload)

    if response.status_code == 200:
        login_pass = [email, password, name]

    token = response.json()['accessToken']
    id_order = ApiMethods.create_order(email, password, Ingredient.list_of_ingredients)
    login_pass = [email, password, name, id_order]

    return login_pass