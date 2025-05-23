import allure
import requests
from curl import urls


class ApiMethods:

    @staticmethod
    @allure.step('Создаем пользователя.')
    def create_user(email_new: str, password_new: str, name_new : str):
        return requests.post(urls.USER_REGISTER_HANDLE, json={"email": email_new, "password": password_new, "name": name_new })

    @staticmethod
    @allure.step('Авторизуемся под логином пользователя.')
    def login_user(email_user: str, password_user: str):
        return requests.post(urls.USER_REGISTER_HANDLE, json={"email": email_user, "password": password_user})

    @staticmethod
    @allure.step('Удаляем созданного пользователя.')
    def delete_user(email_delete, password_delete, name_delete):
        token_response = requests.post(urls.USER_LOGIN_HANDLE, json={"email": email_delete, "password": password_delete, "name": name_delete})
        token = token_response.json()['accessToken']
        return requests.delete(urls.USER_DATA_HANDLE, headers={'Authorization': token})

    @staticmethod
    @allure.step('Создаем новый заказ авторизованным пользователем.')
    def create_order(email_user, password_user, ingredients):
        response = requests.post(urls.USER_LOGIN_HANDLE, json={"email": email_user, "password": password_user})
        token = response.json()['accessToken']
        id_order = requests.post(urls.ORDERS_HANDLE, json={"ingredients": ingredients}, headers={'Authorization': token}).json()['order']['number']
        return id_order