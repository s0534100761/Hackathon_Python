import allure
import requests
import test_cases.conftest


class APIActions:

    @staticmethod
    @allure.step("Get request")
    def get_server(url, value):
        response = requests.get(url + value)
        return response.json()

    @staticmethod
    @allure.step("Post request")
    def post_params(url, value, params):
        response = requests.post(url + value, json=params, headers=test_cases.conftest.header)
        return response.status_code

    @staticmethod
    @allure.step("Delete request")
    def delete_post(url, value, id):
        response = requests.delete(url + value + id)
        return response


